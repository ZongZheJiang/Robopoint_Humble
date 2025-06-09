# Hardware  Requirements

Intel RealSense Depth Camera D435i

# How to Run

pip install -r requirements.txt
source /opt/ros/humble/setup.bash
colcon build
source install/setup.bash
ros2 launch robot_startup full_system.launch.py