#!/usr/bin/env python3
import rospy
from publisher_subscriber.msg import Complex


def callback(msg):
 print('Real: ', msg.real)
 print('Imaginary: ', msg.imaginary)

rospy.init_node('complex_sub')
sub = rospy.Subscriber('complex', Complex, callback)
rospy.spin()
