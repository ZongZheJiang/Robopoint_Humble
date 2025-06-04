from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import PathJoinSubstitution

def generate_launch_description():

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
            'depth_module.profile': '640x480x30', 
            'rgb_camera.profile': '640x480x30',
            'initial_reset': 'true'
            # You can find available parameters by running:
            # ros2 launch realsense2_camera rs_launch.py --show-args
        }.items()
    )

    image_projector_node = Node(
        package='image_projector',
        namespace='image_projector', # Namespacing helps avoid topic/service clashes
        executable='image_projector',
        output='screen'
    )

    move_arm_node = Node(
        package='robot_control',
        namespace='robot_control',
        executable='move_arm',
        output='screen'
    )

    query_node = Node(
        package='robopoint_llm',
        namespace='robopoint_llm',
        executable='query',
        output='screen'
    )

    realsense_node = Node(
        package='image_projector',
        namespace='realsense_node',
        executable='realsense_projector',
        output='screen'
    )

    ld = LaunchDescription()

    ld.add_action(interbotix_xsarm_launch)
    ld.add_action(realsense_camera_launch)
    ld.add_action(realsense_node)
    ld.add_action(image_projector_node)
    ld.add_action(query_node)
    ld.add_action(move_arm_node)

    return ld