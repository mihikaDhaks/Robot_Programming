#!/usr/bin/env python3

import rospy
from publisher_subscriber.msg import HWstatus

if __name__=='__main__':
    rospy.init_node("hw_pub")
    
    pub = rospy.Publisher("hardware_status", HWstatus, queue_size=10)

    rate = rospy.Rate(5)

    while not rospy.is_shutdown():
        msg= HWstatus()
        msg.temperature =45
        msg.are_motors_up = True
        msg.debug_message = "Everything is running well"
        pub.publish(msg)
        rate.sleep()
