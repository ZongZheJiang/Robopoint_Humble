"""
This is a reference file that hooks directly into pyrealsense2
However, pyrealsense cannot work concurrently with ROS2 since resource cannot be shared
Therefore its going to be entirely ROS2 implementation
"""


import rclpy
from rclpy.node import Node
import pyrealsense2.pyrealsense2 as rs
import numpy as np
import cv2

class RealSenseNode(Node):
    def __init__(self):
        super().__init__('realsense_node')
        self.pipeline = rs.pipeline()
        self.config = rs.config()
        self.config.enable_stream(rs.stream.color, 1280, 720, rs.format.bgr8, 30)
        self.config.enable_stream(rs.stream.depth, 1280, 720, rs.format.z16, 30)
        self.pipeline.start(self.config)

    def get_frames(self):
        frames = self.pipeline.wait_for_frames()
        color_frame = frames.get_color_frame()
        depth_frame = frames.get_depth_frame()

        if not color_frame or not depth_frame:
            return None, None

        color_image = np.asanyarray(color_frame.get_data())
        depth_image = np.asanyarray(depth_frame.get_data())

        return color_image, depth_image

    def compute_point_cloud(self, depth_image):
        intrinsics = self.pipeline.get_active_profile().get_stream(rs.stream.depth).as_video_stream_profile().get_intrinsics()
        points = []
        for y in range(depth_image.shape[0]):
            for x in range(depth_image.shape[1]):
                depth = depth_image[y, x]
                if depth == 0:
                    continue
                point = rs.rs2_deproject_pixel_to_point(intrinsics, [x, y], depth)
                points.append(point)
        return np.array(points)

    def run(self):
        while rclpy.ok():
            color_image, depth_image = self.get_frames()
            if color_image is not None and depth_image is not None:
                cv2.imshow("RGB Image", color_image)
                cv2.imshow("Depth Image", depth_image)
                point_cloud = self.compute_point_cloud(depth_image)
                print(f"Point Cloud Shape: {point_cloud.shape}")
                cv2.waitKey(1)

def main(args=None):
    rclpy.init(args=args)
    realsense_node = RealSenseNode()
    try:
        realsense_node.run()
    except KeyboardInterrupt:
        pass
    finally:
        realsense_node.pipeline.stop()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
