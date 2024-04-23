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

mika@mika:~/catkin_ws/src$ catkin_create_pkg publisher_subscriber rospy std_msgs

mika@mika:~/catkin_ws/src$ cd ..

mika@mika:~/catkin_ws$ catkin_make

mika@mika:~/catkin_ws$ cd src

mika@mika:~/catkin_ws/src$ cd publisher_subscriber

mika@mika:~/catkin_ws/src/publisher_subscriber$mkdir msg

mika@mika:~/catkin_ws/src/publisher_subscriber$ cd msg

mika@mika:~/catkin_ws/src/publisher_subscriber/msg$ touch <msg_type>.msg

mika@mika:~/catkin_ws/src/publisher_subscriber/msg$ cd ..

mika@mika:~/catkin_ws/src/publisher_subscriber$ mkdir scripts

mika@mika:~/catkin_ws/src/publisher_subscriber$ cd scripts

mika@mika:~/catkin_ws/src/publisher_subscriber/scripts$ gedit <publisher_name>_pub.py

mika@mika:~/catkin_ws/src/publisher_subscriber/scripts$ gedit <subscriber_name>_sub.py

mika@mika:~/catkin_ws/src/publisher_subscriber/scripts$ chmod +x <publisher_name>_pub.py

mika@mika:~/catkin_ws/src/publisher_subscriber/scripts$ chmod +x <subscriber_name>_sub.py

Building ROS Package
===============================================================================

mika@mika:~/catkin_ws$ catkin_make

Run roscore
===============================================================================

mika@mika:~/catkin_ws/src/publisher_subscriber/scripts$ roscore

PARAMETERS
 * /rosdistro: noetic
 * /rosversion: 1.16.0

Execute Python Files
===============================================================================

mika@mika:~/catkin_ws/src/publisher_subscriber/scripts$ source ~/catkin_ws/devel/setup.bash

mika@mika:~/catkin_ws/src/publisher_subscriber/scripts$ python3 <publisher_name>_pub.py

mika@mika:~/catkin_ws/src/publisher_subscriber/scripts$ python3 <subscriber_name>_sub.py
