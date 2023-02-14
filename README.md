#  robot_localization_tests

Repository with robot localization package basic test in ROS2.

# How to run the test

1. Build the package - ```colcon build```.

2. Source workspace - ```source install/setup.sh```.

3. Run the test - ```ros2 launch robot_localization_tests robot_localization_launch.py```.

4. Check tfs in RViz.

## VS code dev container

* You can find config files for the vs code dev contatiner in the .devcontainer 
folder.
 
* To create the dev container you need to have "Dev Containers" extension in your 
vs code - https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers

* Open vscode in the repository folder, hit ```Ctrl + P``` and choose 
"Dev Containers: Rebuild Container without Cache".

* VS code will automatically create dev container based on the 
"osrf/ros:humble-desktop-full" and will install all the required dependencies.