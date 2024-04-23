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

mika@mika:~/catkin_ws/src$ catkin_create_pkg <package_name> rospy std_msgs

mika@mika:~/catkin_ws/src$ cd ..

mika@mika:~/catkin_ws$ catkin_make

mika@mika:~/catkin_ws$ cd src

mika@mika:~/catkin_ws/src$ cd <package_name>

mika@mika:~/catkin_ws/src/<package_name>$mkdir msg

mika@mika:~/catkin_ws/src/<package_name>$ cd msg

mika@mika:~/catkin_ws/src/<package_name>/msg$ touch <msg_type>.msg

mika@mika:~/catkin_ws/src/<package_name>/msg$ cd ..

mika@mika:~/catkin_ws/src/<package_name>$ mkdir scripts

mika@mika:~/catkin_ws/src/<package_name>$ cd scripts

mika@mika:~/catkin_ws/src/<package_name>/scripts$ gedit <publisher_name>_pub.py

mika@mika:~/catkin_ws/src/<package_name>/scripts$ gedit <subscriber_name>_sub.py

mika@mika:~/catkin_ws/src/<package_name>/scripts$ chmod +x <publisher_name>_pub.py

mika@mika:~/catkin_ws/src/<package_name>/scripts$ chmod +x <subscriber_name>_sub.py

Building ROS Package
===============================================================================

mika@mika:~/catkin_ws$ catkin_make

Run roscore
===============================================================================

mika@mika:~/catkin_ws/src/<package_name>/scripts$ roscore

PARAMETERS
 * /rosdistro: noetic
 * /rosversion: 1.16.0

Execute Python Files
===============================================================================

mika@mika:~/catkin_ws/src/<package_name>/scripts$ source ~/catkin_ws/devel/setup.bash

mika@mika:~/catkin_ws/src/<package_name>/scripts$ python3 complex_pub.py

mika@mika:~/catkin_ws/src/<package_name>/scripts$ python3 complex_sub.py
