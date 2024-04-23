#!/usr/bin/env python3

import rospy
from publisher_subscriber.msg import HWstatus

def callback(msg):
  """
  This function is called whenever a message is received on the subscribed topic.
  It prints the details from the HWstatus message.
  """
  print("Temperature:", msg.temperature)
  print("Motors Up:", msg.are_motors_up)
  print("Debug Message:", msg.debug_message)
  print("---")

if __name__ == '__main__':
  rospy.init_node('hw_sub')
  sub = rospy.Subscriber("hardware_status", HWstatus, callback)
  rospy.spin()
