#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int64

def callback(data):
  
  print(f"Received number: {data.data}")

if __name__ == '__main__':
  rospy.init_node("number_subscriber")

  # Subscribe to the "/number" topic with message type Int64
  sub = rospy.Subscriber("/number", Int64, callback)

  # Keep the subscriber running until ROS is shut down
  rospy.spin()
