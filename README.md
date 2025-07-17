# Hardware  Requirements

Intel RealSense Depth Camera D435i
PX100

# How to Run

`pip install -r requirements.txt`<br>
`source /opt/ros/humble/setup.bash`<br>
`colcon build`<br>
`source install/setup.bash`<br>
`ros2 launch robot_startup full_system.launch.py`<br>

# Modules 

## Computer Generated Modules upon setting up of the workplace (CANNOT BE REMOVED):
1. interbotix_ros_core
2. interbotix_ros_manipulators
3. interbotix_ros_toolboxes
4. moveit_visual_tools

## Components of Set-Up:
- robopoint_llm: a node that calls the trained model to complete the pointing task
- image_projector: a node that controls the Intel RealSense Camera and pre-processes the image before sending to robopoint_llm
- robot_control: takes the response from robopoint_llm and converts them into actionable moves that are carried out by the robot
- robot_startup: a comprehensive launch file within a package that launches all other nodes for easy start-up
- robopoint_interfaces: a folder containing the definitions of various custom messages and services used

# Notes

- MoveIt assumes that the robot has 6 degrees of freedom, but PX100 only has 4 degrees of freedom. Thus, some tweaking needed to be done.
- The current setup uses robopoint-v1-llama-2-7b-lora, which has relatively low accuracy. One way was to use stronger models created by the authors, such as robopoint-v1-vicuna-v.15-13b. Another way is to train a model using the training method given by the authors in the following repo: https://github.com/wentaoyuan/RoboPoint/tree/master 
  - However, training requires the download of their dataset, which is ~300GB. 
  - Streaming the data is a possible alternative, but RoboPoint authors adapted their training pipeline from [lmsys-FastChat](https://github.com/lm-sys/FastChat/tree/main), which necessitates download of dataset. While possible to adapt to data streaming, it requires substantial changes to exisitng training pipeline
- Some areas of improvement for the project include checking whether it supports other models of robots, as well as to improve its accuracy in pointing
- Explored NVILA and [VILA-HD](https://arxiv.org/pdf/2503.19903), preliminary testing indicates that VILA-HD has a different architecture from LLaMA and Vicuna models, but more research can be done to see if substitution can be done
- Dockerising the ROS workspace and running a larger model (such as Vicuna 1.5 13B) is another possible alternative in improving accuracy of pipeline

ROS Documentation: https://docs.ros.org/en/humble/index.html