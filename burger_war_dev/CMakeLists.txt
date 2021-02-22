cmake_minimum_required(VERSION 2.8.3)
project(burger_war_dev)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  geometry_msgs
  control_msgs
	std_msgs
  sensor_msgs
  cv_bridge
  tf
)

add_service_files(
  FILES
  DesiredPose.srv
  VisualFeedbackFlag.srv
)

generate_messages(
  DEPENDENCIES
  std_msgs
  geometry_msgs
)

catkin_package(
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

add_executable(randomRun src/randomRun.cpp)
target_link_libraries(randomRun ${catkin_LIBRARIES})