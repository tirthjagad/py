#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32MultiArray


def callback(msg):
    rospy.loginfo(len(msg.ranges))


rospy.init_node('scan_values')
sub = rospy.Subscriber('LaserData_hokuyo', Float32MultiArray, callback)
rospy.spin()
