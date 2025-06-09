import os
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import PathJoinSubstitution
from ament_index_python.packages import get_package_share_directory

package_name = "robot_startup"

def generate_launch_description():

    pkg_path = get_package_share_directory(package_name)

    rviz_config_file = os.path.join(pkg_path, 'rviz', 'xsarm_description.rviz')

    interbotix_xsarm_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('interbotix_xsarm_control'), # Package containing the launch file
                'launch',
                'xsarm_control.launch.py' # The main launch file for Interbotix arms
            ])
        ]),
        launch_arguments={
            'robot_model': 'px100', 
            'use_sim':'true', 
            'use_rviz': 'true',
            'use_joint_pub_gui': 'true',
            'rviz_config': rviz_config_file
        }.items()
    )

    realsense_camera_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('realsense2_camera'),
                'launch',
                'rs_launch.py'
            ])
        ]),
        launch_arguments={
            'pointcloud.enable': 'true',       
            'align_depth.enable': 'true',     
            'enable_sync': 'true', 
            'enable_rgbd': 'true',
            'enable_color': 'true',
            'enable_depth': 'true',
            'depth_module.profile': '640x480x30', 
            'rgb_camera.profile': '640x480x30',
            'initial_reset': 'true'
            # You can find available parameters by running:
            # ros2 launch realsense2_camera rs_launch.py --show-args
        }.items()
    )

    static_transform_publisher_node = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        name='static_camera_transform_publisher',
        arguments=[
            # Arguments are: x, y, z, qx, qy, qz, qw, parent_frame, child_frame
            # For roll, pitch, yawh, use '0', '0.5', '0.8', '0', '0', '0', 'base_link', 'camera_link'
            '--x', '0.0',
            '--y', '0.3',
            '--z', '0.3',
            '--yaw', '0.0',
            '--pitch', '0.0',
            '--roll', '0.0',
            '--frame-id', 'base_link', # The parent frame
            '--child-frame-id', 'camera_link' # The child frame
        ]
    )

    image_projector_node = Node(
        package='image_projector',
        executable='image_projector',
        output='screen'
    )

    move_arm_node = Node(
        package='robot_control',
        executable='move_arm',
        output='screen'
    )

    query_node = Node(
        package='robopoint_llm',
        executable='query',
        output='screen',
        arguments=['--filepath', "/home/evas/interbotix_ws/debug.jpg"]
    )

    ld = LaunchDescription()

    ld.add_action(interbotix_xsarm_launch)
    ld.add_action(realsense_camera_launch)
    ld.add_action(static_transform_publisher_node)
    ld.add_action(image_projector_node)
    ld.add_action(query_node)
    ld.add_action(move_arm_node)

    return ld