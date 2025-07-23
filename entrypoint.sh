#!/bin/bash
set -e

# Source ROS 2 setup
source /opt/ros/humble/setup.bash

if [ -f "/root/interbotix_ws/install/setup.bash" ]; then
  source "/root/interbotix_ws/install/setup.bash"
else
  echo "WARNING: Base workspace setup file not found at /root/interbotix_ws/install/setup.bash"
fi

# Execute the command passed to this script
exec "$@"