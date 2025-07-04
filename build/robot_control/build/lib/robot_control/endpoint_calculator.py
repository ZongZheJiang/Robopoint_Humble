import rclpy
from rclpy.node import Node
from robopoint_interfaces.srv import Get3DCoordinates, MoveToPoint
import tf2_ros
import tf2_geometry_msgs
from geometry_msgs.msg import PointStamped
from interbotix_xs_modules.xs_robot.arm import InterbotixManipulatorXS
from std_msgs.msg import Float32MultiArray
import math

class EndpointCalculatorNode(Node):

    def __init__(self):
        super().__init__('endpoint_calculator_node')

        self.coordinates_subscriber = self.create_subscription(
            
        )
