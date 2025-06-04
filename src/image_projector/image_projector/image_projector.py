import rclpy
from rclpy.node import Node
from sensor_msgs.msg import CameraInfo
from realsense2_camera_msgs.msg import RGBD
from cv_bridge import CvBridge
from robopoint_interfaces.srv import Get3DCoordinates
import numpy as np
from image_geometry import PinholeCameraModel

"""
Run this service with the following command:
    ros2 run image_projector service
"""

class RGBDSubscriber(Node):
    def __init__(self):
        super().__init__('rgbd_subscriber')

        # Subscribe to the RGBD topic
        self.subscription = self.create_subscription(
            RGBD,
            '/camera/camera/rgbd',
            self.listener_callback,
            10
        )
        # Subscribe to the camera info topic using the aligned depth stream
        self.camera_info_subscription = self.create_subscription(
            CameraInfo,
            '/camera/camera/aligned_depth_to_color/camera_info',
            self.camera_info_callback,
            10
        )
        self.bridge = CvBridge()

        # Class variables
        self.rgb_image = None
        self.depth_image = None
        self.cam_model = None
        self.srv = self.create_service(
            Get3DCoordinates, 
            'get_3d_coordinates', 
            self.get_3d_coordinates_callback
        )

    def camera_info_callback(self, msg: CameraInfo):
        # Create and initialize the pinhole camera model with the latest camera info.
        self.cam_model = PinholeCameraModel()
        self.cam_model.fromCameraInfo(msg)

    def listener_callback(self, msg: RGBD):
        '''Callback function for the RGBD subscriber to receive RGB and depth images.'''
        try:
            self.rgb_image = self.bridge.imgmsg_to_cv2(msg.rgb, desired_encoding='bgr8')
        except Exception as e:
            self.get_logger().error("Error converting RGB image: {}".format(e))
            return

        try:
            self.depth_image = self.bridge.imgmsg_to_cv2(msg.depth, desired_encoding='passthrough')
        except Exception as e:
            self.get_logger().error("Error converting depth image: {}".format(e))
            return



    def get_3d_coordinates_callback(self, request, response):
        """
        Takes in the incoming coordinates (request.x, request.y) from the user and applies transforms.
        Returns the 3D point in space from perspective of the depth cam
        """

        # Ensure images and camera info have been received
        if self.rgb_image is None or self.depth_image is None:
            self.get_logger().error("No images received.")
            return response

        if self.cam_model is None:
            self.get_logger().error("Camera intrinsics not set yet.")
            return response

        u, v = request.x, request.y

        # The incoming x and y coordinates are from the range of [0, 1], per RoboPoint's output
        # Convert them to pixel coordinates by multiplying with the image dimensions.
        u = int(u * self.rgb_image.shape[1])
        v = int(v * self.rgb_image.shape[0])

        # Check if the coordinates are within image bounds, though this should not be necessary due to above step
        # if u < 0 or u >= self.rgb_image.shape[1] or v < 0 or v >= self.rgb_image.shape[0]:
        #     self.get_logger().error("Coordinates out of image bounds.")
        #     return response

        # Get the depth value from the depth image at pixel (u, v)
        depth_value = self.depth_image[v, u]
        self.get_logger().info(f"Depth image:\n{self.depth_image}")
        # A common issue: depth_image might be scaled (e.g., in millimeters instead of meters);
        # ensure that the depth unit is in meters or apply the appropriate conversion.
        if np.isnan(depth_value) or depth_value == 0:
            self.get_logger().error("Invalid depth value at the given coordinates.")
            return response

        # Use the image_geometry method to get a 3D ray from the pixel coordinates.
        # This method automatically handles undistortion (if necessary) and returns
        # a unit vector pointing from the camera center in the direction of (u,v).
        ray = self.cam_model.projectPixelTo3dRay((u, v))

        # Multiply the unit vector by the depth to get the 3D coordinate.
        # Note: This assumes the depth is the distance along the ray direction.
        x_3d = ray[0] * depth_value
        y_3d = ray[1] * depth_value
        z_3d = ray[2] * depth_value

        response.x = float(x_3d)
        response.y = float(y_3d)
        response.z = float(z_3d)

        return response

def main(args=None):
    rclpy.init(args=args)
    rgbd_subscriber = RGBDSubscriber()
    rclpy.spin(rgbd_subscriber)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
