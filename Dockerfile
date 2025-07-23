# Filename: Dockerfile
#
# This Dockerfile builds the lightweight OVERLAY image for active development.
# It uses the pre-built base image and adds your specific application code.
# It DEFINES THE ENTRYPOINT for the final application.

# Tag your base image as 'turtlebot3-base' or use a registry path.
FROM zongzhejiang/robopoint_ws:humble

ARG ROS_DISTRO=humble
ENV ROS_DISTRO=${ROS_DISTRO}
SHELL ["/bin/bash", "-c"]

# Create an overlay Colcon workspace
WORKDIR /root/interbotix_ws

COPY ./reqs.txt .

RUN pip install --no-cache-dir -r reqs.txt

COPY ./src/robopoint_interfaces/ ./src/robopoint_interfaces/
COPY ./src/robopoint_llm/ ./src/robopoint_llm/
COPY ./src/robot_control/ ./src/robot_control/
COPY ./src/robot_startup/ ./src/robot_startup/
COPY ./src/image_projector/ ./src/image_projector/
COPY ./debug.jpg .
COPY ./point_viz.py .
COPY commands.txt .
COPY troubleshooting.txt .

# Build the overlay. It's fast because all heavy dependencies are in the base.
# We source the base workspace to make its packages available during the build.
RUN source /root/interbotix_ws/install/setup.bash \
 && colcon build 

# Set up the entrypoint that sources ALL workspaces correctly.
# This is the correct place for the ENTRYPOINT definition.
COPY ./entrypoint.sh /
RUN chmod +x /entrypoint.sh
ENTRYPOINT [ "/entrypoint.sh" ]

CMD ["bash"]