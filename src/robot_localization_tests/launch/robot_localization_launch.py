#! /usr/bin/env python
import os
import launch
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions          import Node
from launch.substitutions        import Command

BAG_FILE_NAME = "vn_bag_1676206208.6288934.bag_0.db3"

def generate_launch_description():
  pkg_path = get_package_share_directory("robot_localization_tests")

  launch_description = launch.LaunchDescription()
  add_navsat_transform_node(launch_description, pkg_path)
  add_robot_localization_node(launch_description, pkg_path)
  add_rosbag_play_node(launch_description, pkg_path)
  add_rviz_node(launch_description, pkg_path)
  return launch_description

def add_navsat_transform_node(launch_description, pkg_path):
  navsat_transform_config = os.path.join(
    pkg_path, "config/navsat_transform_config.yaml")

  navsat_transform_node = Node(
    package    = 'robot_localization',
    executable = 'navsat_transform_node',
    name       = 'navsat_transform',
    parameters = [navsat_transform_config],
    arguments  = ['--ros-args', '--log-level', 'warn']
  )

  launch_description.add_action(navsat_transform_node)

def add_robot_localization_node(launch_description, pkg_path):
  robot_localization_config = os.path.join(pkg_path, "config/ekf_with_gps.yaml")

  robot_localization_node = Node(
    package    = 'robot_localization',
    executable = 'ekf_node',
    name       = 'ekf_filter_node',
    output     = 'screen',
    parameters = [robot_localization_config]
  )
  
  launch_description.add_action(robot_localization_node)

def add_rviz_node(launch_description, pkg_path):
  rviz_config = os.path.join(pkg_path, "config/bag_analysis.rviz")

  rviz = Node(
    package    = 'rviz2',
    executable = 'rviz2',
    output     = 'screen',
    arguments  = ['-d', rviz_config]
  ) 

  launch_description.add_action(rviz)

def add_rosbag_play_node(launch_description, pkg_path):
  bag_file = os.path.join(pkg_path, "test_data", BAG_FILE_NAME)

  rosbag_play = launch.actions.ExecuteProcess(
    cmd = ['ros2', 'bag', 'play', bag_file, '--clock'],
    output='screen'
  )

  launch_description.add_action(rosbag_play)