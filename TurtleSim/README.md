Creating Workspace
===============================================================================

mika@mika:~$ mkdir catkin_ws

mika@mika:~$ cd catkin_ws

mika@mika:~/catkin_ws$ mkdir src

mika@mika:~/catkin_ws$ catkin_make

mika@mika:~/catkin_ws$ cd devel

mika@mika:~/catkin_ws/devel$ source setup.bash

mika@mika:~/catkin_ws/devel$ gedit ~/.bashrc

Creating Package
===============================================================================

mika@mika:~$ cd catkin_ws

mika@mika:~/catkin_ws$ cd src

mika@mika:~/catkin_ws/src$ catkin_create_pkg TurtleSim rospy std_msgs

mika@mika:~/catkin_ws/src$ cd ..

mika@mika:~/catkin_ws$ catkin_make

mika@mika:~/catkin_ws$ cd src

mika@mika:~/catkin_ws/src$ cd TurtleSim

mika@mika:~/catkin_ws/src/TurtleSim$ mkdir scripts

mika@mika:~/catkin_ws/src/TurtleSim$ cd scripts

mika@mika:~/catkin_ws/src/TurtleSim/scripts$ gedit <draw_shape>.py

mika@mika:~/catkin_ws/src/TurtleSim/scripts$ chmod +x <draw_shape>.py


Building ROS Package
===============================================================================

mika@mika:~/catkin_ws$ catkin_make

Run roscore
===============================================================================

mika@mika:~/catkin_ws/src/TurtleSim/scripts$ roscore

PARAMETERS
 * /rosdistro: noetic
 * /rosversion: 1.16.0
   
Run Turtlesim
===============================================================================

mika@mika:~/catkin_ws/src/TurtleSim/scripts$ rosrun turtlesim turtlesim_node

Execute Python Files
===============================================================================

mika@mika:~/catkin_ws/src/TurtleSim/scripts$ source ~/catkin_ws/devel/setup.bash

mika@mika:~/catkin_ws/src/TurtleSim/scripts$ python3 <draw_shape>.py

