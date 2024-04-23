Creating Workspace
===============================================================================

mkdir catkin_ws

cd catkin_ws

mkdir src

catkin_make

ls

cd devel

source setup.bash

gedit ~/.bashrc

Creating Package
===============================================================================

mika@mika:~$ cd catkin_ws
mika@mika:~/catkin_ws$ cd src
mika@mika:~/catkin_ws/src$ catkin_create_pkg publisher_subscriber rospy std_msgs
Created file publisher_subscriber/package.xml
Created file publisher_subscriber/CMakeLists.txt
Created folder publisher_subscriber/src
Successfully created files in /home/mika/catkin_ws/src/publisher_subscriber. Please adjust the values in package.xml.
mika@mika:~/catkin_ws/src$ cd ..
mika@mika:~/catkin_ws$ catkin_make
Base path: /home/mika/catkin_ws
Source space: /home/mika/catkin_ws/src
Build space: /home/mika/catkin_ws/build
Devel space: /home/mika/catkin_ws/devel
Install space: /home/mika/catkin_ws/install
####
#### Running command: "cmake /home/mika/catkin_ws/src -DCATKIN_DEVEL_PREFIX=/home/mika/catkin_ws/devel -DCMAKE_INSTALL_PREFIX=/home/mika/catkin_ws/install -G Unix Makefiles" in "/home/mika/catkin_ws/build"
####
-- Using CATKIN_DEVEL_PREFIX: /home/mika/catkin_ws/devel
-- Using CMAKE_PREFIX_PATH: /opt/ros/noetic
-- This workspace overlays: /opt/ros/noetic
-- Found PythonInterp: /usr/bin/python3 (found suitable version "3.8.10", minimum required is "3") 
-- Using PYTHON_EXECUTABLE: /usr/bin/python3
-- Using Debian Python package layout
-- Using empy: /usr/lib/python3/dist-packages/em.py
-- Using CATKIN_ENABLE_TESTING: ON
-- Call enable_testing()
-- Using CATKIN_TEST_RESULTS_DIR: /home/mika/catkin_ws/build/test_results
-- Forcing gtest/gmock from source, though one was otherwise available.
-- Found gtest sources under '/usr/src/googletest': gtests will be built
-- Found gmock sources under '/usr/src/googletest': gmock will be built
-- Found PythonInterp: /usr/bin/python3 (found version "3.8.10") 
-- Using Python nosetests: /usr/bin/nosetests3
-- catkin 0.8.10
-- BUILD_SHARED_LIBS is on
-- BUILD_SHARED_LIBS is on
-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-- ~~  traversing 1 packages in topological order:
-- ~~  - publisher_subscriber
-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-- +++ processing catkin package: 'publisher_subscriber'
-- ==> add_subdirectory(publisher_subscriber)
-- Configuring done
-- Generating done
-- Build files have been written to: /home/mika/catkin_ws/build
####
#### Running command: "make -j1 -l1" in "/home/mika/catkin_ws/build"
####
mika@mika:~/catkin_ws$ cd src
mika@mika:~/catkin_ws/src$ cd publisher_subscriber
mika@mika:~/catkin_ws/src/publisher_subscriber$mkdir msg
mika@mika:~/catkin_ws/src/publisher_subscriber$ cd msg
mika@mika:~/catkin_ws/src/publisher_subscriber/msg$ touch Complex.msg
mika@mika:~/catkin_ws/src/publisher_subscriber/msg$ cd ..
mika@mika:~/catkin_ws/src/publisher_subscriber$ mkdir scripts
mika@mika:~/catkin_ws/src/publisher_subscriber$ cd scripts
mika@mika:~/catkin_ws/src/publisher_subscriber/scripts$ gedit complex_pub.py
^C
mika@mika:~/catkin_ws/src/publisher_subscriber/scripts$ gedit complex_sub.py
^C
mika@mika:~/catkin_ws/src/publisher_subscriber/scripts$ chmod +x complex_pub.py
mika@mika:~/catkin_ws/src/publisher_subscriber/scripts$ chmod +x complex_sub.py

Building ROS Package
===============================================================================

mika@mika:~/catkin_ws$ catkin_make
Base path: /home/mika/catkin_ws
Source space: /home/mika/catkin_ws/src
Build space: /home/mika/catkin_ws/build
Devel space: /home/mika/catkin_ws/devel
Install space: /home/mika/catkin_ws/install
####
#### Running command: "make cmake_check_build_system" in "/home/mika/catkin_ws/build"
####
-- Using CATKIN_DEVEL_PREFIX: /home/mika/catkin_ws/devel
-- Using CMAKE_PREFIX_PATH: /opt/ros/noetic
-- This workspace overlays: /opt/ros/noetic
-- Found PythonInterp: /usr/bin/python3 (found suitable version "3.8.10", minimum required is "3") 
-- Using PYTHON_EXECUTABLE: /usr/bin/python3
-- Using Debian Python package layout
-- Using empy: /usr/lib/python3/dist-packages/em.py
-- Using CATKIN_ENABLE_TESTING: ON
-- Call enable_testing()
-- Using CATKIN_TEST_RESULTS_DIR: /home/mika/catkin_ws/build/test_results
-- Forcing gtest/gmock from source, though one was otherwise available.
-- Found gtest sources under '/usr/src/googletest': gtests will be built
-- Found gmock sources under '/usr/src/googletest': gmock will be built
-- Found PythonInterp: /usr/bin/python3 (found version "3.8.10") 
-- Using Python nosetests: /usr/bin/nosetests3
-- catkin 0.8.10
-- BUILD_SHARED_LIBS is on
-- BUILD_SHARED_LIBS is on
-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-- ~~  traversing 1 packages in topological order:
-- ~~  - publisher_subscriber
-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-- +++ processing catkin package: 'publisher_subscriber'
-- ==> add_subdirectory(publisher_subscriber)
-- Using these message generators: gencpp;geneus;genlisp;gennodejs;genpy
-- publisher_subscriber: 1 messages, 0 services
-- Configuring done
-- Generating done
-- Build files have been written to: /home/mika/catkin_ws/build
####
#### Running command: "make -j1 -l1" in "/home/mika/catkin_ws/build"
####
[  0%] Built target _publisher_subscriber_generate_messages_check_deps_Complex
[  0%] Built target std_msgs_generate_messages_py
[ 28%] Built target publisher_subscriber_generate_messages_py
[ 28%] Built target std_msgs_generate_messages_eus
[ 57%] Built target publisher_subscriber_generate_messages_eus
[ 57%] Built target std_msgs_generate_messages_lisp
[ 71%] Built target publisher_subscriber_generate_messages_lisp
[ 71%] Built target std_msgs_generate_messages_nodejs
[ 85%] Built target publisher_subscriber_generate_messages_nodejs
[ 85%] Built target std_msgs_generate_messages_cpp
[100%] Built target publisher_subscriber_generate_messages_cpp
[100%] Built target publisher_subscriber_generate_messages

Run roscore
===============================================================================

mika@mika:~/catkin_ws/src/publisher_subscriber/scripts$ roscore
... logging to /home/mika/.ros/log/85e401e0-0144-11ef-ad78-812bbe4cefea/roslaunch-mika-5241.log
Checking log directory for disk usage. This may take a while.
Press Ctrl-C to interrupt
Done checking log file disk usage. Usage is <1GB.

started roslaunch server http://mika:40545/
ros_comm version 1.16.0


SUMMARY
========

PARAMETERS
 * /rosdistro: noetic
 * /rosversion: 1.16.0

NODES

auto-starting new master
process[master]: started with pid [5251]
ROS_MASTER_URI=http://mika:11311/

setting /run_id to 85e401e0-0144-11ef-ad78-812bbe4cefea
process[rosout-1]: started with pid [5261]
started core service [/rosout]

Execute Python Files
===============================================================================

mika@mika:~/catkin_ws/src/publisher_subscriber/scripts$ source ~/catkin_ws/devel/setup.bash
mika@mika:~/catkin_ws/src/publisher_subscriber/scripts$ chmod +x complex_pub.py
mika@mika:~/catkin_ws/src/publisher_subscriber/scripts$ python3 complex_pub.py
mika@mika:~/catkin_ws/src/publisher_subscriber/scripts$ python3 complex_sub.py

