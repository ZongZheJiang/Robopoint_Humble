import rclpy.logging
from robopoint_interfaces.srv import Query, MoveToPoint

import rclpy
from rclpy.node import Node
from realsense2_camera_msgs.msg import RGBD
from cv_bridge import CvBridge
from torch import rsub
from transformers.models import llama
from robopoint.run_llm_service import llm_service
from rclpy.utilities import remove_ros_args

# deps to convert cv2 to PIL
import cv2
from PIL import Image
import numpy as np

# CLI tools
import sys
import argparse

# To run this node, activate camera first
# ros2 launch realsense2_camera rs_launch.py enable_rgbd:=true enable_sync:=true align_depth.enable:=true enable_color:=true enable_depth:=true
# then run in another terminal (with filepath for debugging)
# ros2 run robopoint_llm query --filepath /home/evas/interbotix_ws/debug.jpg
#
# finally, call the service (ignore the args below)
# ros2 service call /query_service robopoint_interfaces/srv/Query "{query: 'You might not see anything, but point right at the center of the image'}"

class QueryService(Node):
    """Gets an image from the RGBD node and passes it to the LLM calling node"""
    def __init__(self, filepath=None):
        super().__init__('query_service_node')
        # debug args
        self.filepath = filepath

        # Subscribe to the RGBD topic
        self.subscription = self.create_subscription(
            RGBD,
            '/camera/camera/rgbd',
            self.listener_callback,
            1 # only need the latest image
        )
        self.bridge = CvBridge()
        self.rgb_image = None
        self.move_to_point_client = self.create_client(
            MoveToPoint, 
            'move_to_point'
        )

        while not self.move_to_point_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info("service not available, waiting again... ")
        
        self.srv = self.create_service(
            Query, 
            'query_service', 
            self.query_callback
        )

    def listener_callback(self, msg: RGBD):
        '''Callback function for the RGBD subscriber to receive RGB and depth images.'''
        try:
            self.rgb_image = self.bridge.imgmsg_to_cv2(msg.rgb, desired_encoding='bgr8')
            # self.get_logger().info("Received RGB image")
        except Exception as e:
            self.get_logger().error("Error converting RGB image: {}".format(e))
            return

    def query_callback(self, request, response):
        '''Callback function for the query service to receive a query and return a response.'''
        self.get_logger().info(f'Incoming query (prompt)\n-----\n{request.query}')

        if self.rgb_image is None:
            self.get_logger().error("No RGB image received yet")
            return response

        # Convert to PIL image for downstream processing
        img = Image.fromarray(cv2.cvtColor(self.rgb_image, cv2.COLOR_BGR2RGB))

        # read run_llm_service for info - right now I only support 1 image.
        x, y = llm_service.generate(request.query, [img]) # returned as normalized coordinates from 0 to 1

        # Save debug image
        if self.filepath:
            llm_service.process_and_visualize_output([x,y], img, self.filepath)
        # Pass coordinates downstream
        move_to_point_request = MoveToPoint.Request()
        move_to_point_request.x = x
        move_to_point_request.y = y
        try:
            self.get_logger().info(f"Will call call_async with {move_to_point_request}")
            future = self.move_to_point_client.call_async(move_to_point_request)
        except Exception as e:
            print(f"Error: {e}")

        # by right, future returns no result, since the action is that the robot moves.
        return future


def main(args=None):

    rclpy.init(args=args)

    remaining_argv = remove_ros_args(args=sys.argv)

    # if args is None:
    #     args = sys.argv[1:]
    # args = sys.argv[1:]

    parser = argparse.ArgumentParser(
        description='Query service node',
        prog=remaining_argv[0]
    )
    parser.add_argument(
        '--filepath', 
        type=str, 
        help='Absolute filepath to save a debug image to'
    )

    parsed_args = parser.parse_args(args=remaining_argv[1:])
    
    # print(f"parsed args: {parsed_args}")
    # rclpy.logging.get_logger('query').info(f"parsed args: {parsed_args}")

    node_logger = rclpy.logging.get_logger('query_main') # Get a logger
    node_logger.info(f"Parsed custom args: filepath='{parsed_args.filepath}'")
    print(f"PRINT from main: Parsed custom args: filepath='{parsed_args.filepath}'")

    query_service = QueryService(parsed_args.filepath)
    try: 
        rclpy.spin(query_service)
    except KeyboardInterrupt:
        node_logger.info("Keyboard interrupt, shutting down.")
    finally: 
        query_service.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
