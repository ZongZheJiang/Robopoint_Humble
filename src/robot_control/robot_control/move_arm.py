import rclpy
from rclpy.node import Node
from robopoint_interfaces.srv import Get3DCoordinates, MoveToPoint
import tf2_ros
import tf2_geometry_msgs
from geometry_msgs.msg import PointStamped
from interbotix_xs_modules.xs_robot.arm import InterbotixManipulatorXS
from std_msgs.msg import Float32MultiArray
import math

"""interbotix_ros_toolboxes.interbotix_xs_toolbox.interbotix_xs_modules.i
We will need to set up a camera frame (camera_link) manually while testing to provide a reference of where the physical camera is
located in the robot's base frame (px100/base_link).

First run the rviz (not in tmux) with
ros2 launch interbotix_xsarm_descriptions xsarm_description.launch.py robot_model:=px100 use_joint_pub_gui:=true

Then run the following command to set up the camera frame (camera_link) in the robot's base frame (px100/base_link):

ros2 run tf2_ros static_transform_publisher fwd_offset left_offset height_offset 0 0 0 px100/base_link camera_link
^ e.g. ros2 run tf2_ros static_transform_publisher 0.0 0.15 0.1 0 0 0 px100/base_link camera_link
"""


class MoveArmNode(Node):
    """
    This node provides a 'move_to_point' service that:
      1) Receives normalized (0..1) image coordinates (x, y).
      2) Calls 'get_3d_coordinates' to obtain the point in the 'camera_link' frame.
      3) Transforms that point into the 'base_link' frame using tf2.
      4) Commands the Interbotix arm to move its end-effector to this location.
    """
    
    def __init__(self):
        super().__init__('move_arm_node')

        # Create a TF buffer and listener to handle lookup_transform
        self.tf_buffer = tf2_ros.Buffer()
        self.tf_listener = tf2_ros.TransformListener(self.tf_buffer, self)

        # Create a client for the get_3d_coordinates service
        self.get_3d_coordinates_client = self.create_client(
            Get3DCoordinates,
            'get_3d_coordinates'
        )

        self.desired_joint_states_subscription = self.create_subscription(
            Float32MultiArray,
            'desired_joint_states',
            self.listener_callback,
            10
        )

        # Create and start service server for "move_to_point"
        # this is service name, different from node name
        self.move_to_point_srv = self.create_service(
            MoveToPoint,
            'move_to_point',
            self.move_to_point_callback
        )

        # Create the Interbotix arm object (adjust robot type/model as needed)
        self.bot = InterbotixManipulatorXS("px100", "arm", "gripper")

        self.get_logger().info("MoveArmNode is up and running.")
    

    def listener_callback(self, msg):
        pass
        # TODO: process the received information to be sent to /px100/joint_states 

    
    def move_to_point_callback(self, request, response):
        """
        1) Uses request.x and request.y (normalized coords) to call 'get_3d_coordinates'.
        2) Transforms the returned point from 'camera_link' to 'base_link' frame.
        3) Commands the robot arm to move to that 3D location (x, y, z).
        """
        # Ensure service is available
        if not self.get_3d_coordinates_client.wait_for_service(timeout_sec=3.0):
            self.get_logger().error("Service [get_3d_coordinates] not available.")
            response.success = False
            return response

        # 1) Call get_3d_coordinates to retrieve 3D point in camera frame
        self.get_logger().info(f"Received move_to_point request at normalized coords: ({request.x}, {request.y})")
        get_coords_request = Get3DCoordinates.Request()
        get_coords_request.x = request.x
        get_coords_request.y = request.y

        future = self.get_3d_coordinates_client.call_async(get_coords_request)
        rclpy.spin_until_future_complete(self, future)

        if future.result() is None:
            self.get_logger().error("Failed to call get_3d_coordinates service.")
            response.success = False
            return response
        camera_coords = future.result()  # x, y, z in camera frame
        self.get_logger().info(f"3D point in camera frame: {camera_coords.x:.3f}, {camera_coords.y:.3f}, {camera_coords.z:.3f}")

        # 2) Transform the point from camera_link to base_link using TF
        point_in_camera = PointStamped()
        point_in_camera.header.stamp = self.get_clock().now().to_msg()
        point_in_camera.header.frame_id = "camera_link"  # Update if your camera’s frame is different
        point_in_camera.point.x = camera_coords.x
        point_in_camera.point.y = camera_coords.y
        point_in_camera.point.z = camera_coords.z

        try:
            transform = self.tf_buffer.lookup_transform(
                "base_link",     # target frame
                "camera_link",   # source frame
                self.get_clock().now(),  # look up latest transform
            )
        except Exception as ex:
            self.get_logger().error(f"Failed to look up transform from camera_link to base_link: {ex}")
            response.success = False
            return response

        point_in_base = tf2_geometry_msgs.do_transform_point(point_in_camera, transform)
        bx = point_in_base.point.x
        by = point_in_base.point.y
        bz = point_in_base.point.z

        self.get_logger().info(f"Transformed 3D point in base_link frame: ({bx:.3f}, {by:.3f}, {bz:.3f})")

        # 3) Command the Interbotix arm to move to {bx, by, bz}
        try:
            # Example: Move using set_ee_pose_components
            # Additional orientation, pitch, or roll can be specified if needed
            # self.bot.arm.set_ee_pose_components(x=bx, y=by, z=bz)
            # self.get_logger().info("Move command sent to robot arm.")
            pass
            print("DID NOT ACTUALLY MOVE ARM - TESTING")
            response.success = True
        except Exception as e:
            self.get_logger().error(f"Arm motion failed: {e}")
            response.success = False

        return response    


def main(args=None):
    print('Hi from robot_control.')
    rclpy.init(args=args)
    node = MoveArmNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
