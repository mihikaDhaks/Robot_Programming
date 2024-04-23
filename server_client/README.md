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

mika@mika:~/catkin_ws/src$ catkin_create_pkg server_client roscpp rospy std_msgs

mika@mika:~/catkin_ws/src$ cd ..

mika@mika:~/catkin_ws$ catkin_make

mika@mika:~/catkin_ws$ cd src

mika@mika:~/catkin_ws/src$ cd server_client

mika@mika:~/catkin_ws/src/server_client$mkdir srv

mika@mika:~/catkin_ws/src/server_client$ cd srv

mika@mika:~/catkin_ws/src/server_client/srv$ touch <srv_type>.msg

mika@mika:~/catkin_ws/src/server_client/srv$ cd ..

mika@mika:~/catkin_ws/src/server_client$ mkdir scripts

mika@mika:~/catkin_ws/src/server_client$ cd scripts

mika@mika:~/catkin_ws/src/server_client/scripts$ gedit <server_name>_server.py

mika@mika:~/catkin_ws/src/server_client/scripts$ gedit <client_name>_client.py

mika@mika:~/catkin_ws/src/server_client/scripts$ chmod +x <server_name>_server.py

mika@mika:~/catkin_ws/src/server_client/scripts$ chmod +x <client_name>_client.py

Building ROS Package
===============================================================================

mika@mika:~/catkin_ws$ catkin_make

Run roscore
===============================================================================

mika@mika:~/catkin_ws/src/server_client/scripts$ roscore

PARAMETERS
 * /rosdistro: noetic
 * /rosversion: 1.16.0

Execute Python Files
===============================================================================

mika@mika:~/catkin_ws/src/server_client/scripts$ source ~/catkin_ws/devel/setup.bash

mika@mika:~/catkin_ws/src/server_client/scripts$ python3 <server_name>_server.py

mika@mika:~/catkin_ws/src/server_client/scripts$ python3 <client_name>_client.py
