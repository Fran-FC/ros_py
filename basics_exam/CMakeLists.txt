cmake_minimum_required(VERSION 2.8.3)
project(basics_exam)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  std_msgs 
  actionlib_msgs
  geometry_msgs
)

## Generate actions in the 'action' folder
add_action_files(
   FILES
   record_odom.action
 )

## Generate added messages and services with any dependencies listed here
generate_messages(
   DEPENDENCIES
   std_msgs actionlib_msgs geometry_msgs
 )

catkin_package(
 CATKIN_DEPENDS rospy
)

## Specify additional locations of header files
## Your package locations should be listed before other locations
# include_directories(include)
include_directories(
  ${catkin_INCLUDE_DIRS}
)
