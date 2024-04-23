#!/usr/bin/env python3

import rospy
from publisher_subscriber.msg import HardwareStatus

if __name__=='__main__':
    rospy.init_node("hw_status")
    
    pub = rospy.Publisher("hardware_status", HardwareStatus, queue_size=10)

    rate = rospy.Rate(5)

    while not rospy.is_shutdown():
        msg= HardwareStatus()
        msg.temperature =45
        msg.are_motors_up = True
        msg.debug_message = "Everything is running well"
        pub.publish(msg)
        rate.sleep()
