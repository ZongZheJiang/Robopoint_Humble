# Hardware  Requirements

Intel RealSense Depth Camera D435i

# How to Run

`pip install -r requirements.txt`<br>
`source /opt/ros/humble/setup.bash`<br>
`colcon build`<br>
`source install/setup.bash`<br>
`ros2 launch robot_startup full_system.launch.py`<br>

# Modules 

Computer Generated Modules upon setting up of the workplace (CANNOT BE REMOVED):
1. interbotix_ros_core
2. interbotix_ros_manipulators
3. interbotix_ros_toolboxes
4. moveit_visual_tools

Components of Set-Up:
- robopoint_llm: a node that calls the trained model to complete the pointing task
- image_projector: a node that controls the Intel RealSense Camera and pre-processes the image before sending to robopoint_llm
- robot_control: takes the response from robopoint_llm and converts them into actionable moves that are carried out by the robot
- robot_startup: a comprehensive launch file within a package that launches all other nodes for easy start-up
- robopoint_interfaces: a folder containing the definitions of various custom messages and services used

ROS Documentation: https://docs.ros.org/en/humble/index.html