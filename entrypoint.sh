#!/bin/bash
set -e

# Source ROS 2 setup
source /opt/ros/humble/setup.bash

if [ -f "/Robopoint_Humble/install/setup.bash" ]; then
  source "/Robopoint_Humble/install/setup.bash"
  echo "Sourced TurtleBot3 base workspace."
fi

# Execute the command passed to this script
exec "$@"