#!/usr/bin/env python3
import rospy
from publisher_subscriber.msg import Complex
from random import random

rospy.init_node('complex_pub') #creating a node
pub = rospy.Publisher('complex', Complex, queue_size=10)
rate = rospy.Rate(2)
a = float(input("enter values of real part: "))
b = float(input("enter values of imaginary part: "))

while not rospy.is_shutdown():
 msg = Complex()
 msg.real = a
 msg.imaginary =b
 pub.publish(msg)
 rate.sleep()
