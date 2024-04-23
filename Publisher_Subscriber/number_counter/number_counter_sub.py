#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int64

counter = 0

def callback_number(msg):
  global counter
  counter += msg.data
  rospy.loginfo(f"Received number: {msg.data}")
  rospy.loginfo(f"Current counter: {counter}")

def main():
  rospy.init_node('number_counter')
  sub = rospy.Subscriber("/number", Int64, callback_number)
  rospy.spin()

if __name__ == '__main__':
  main()
