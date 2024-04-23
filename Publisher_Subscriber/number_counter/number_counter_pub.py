#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int64

def main():
  rospy.init_node('number_publisher')
  pub = rospy.Publisher("/number", Int64, queue_size=10)
  rate = rospy.Rate(10) # Publish at 10 Hz

  while not rospy.is_shutdown():
    number_to_publish = int(input("Enter a number to publish: "))
    msg = Int64()
    msg.data = number_to_publish
    pub.publish(msg)
    rospy.loginfo(f"Published number: {number_to_publish}")
    rate.sleep()

if __name__ == '__main__':
  main()
