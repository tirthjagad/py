#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Float32
rospy.init_node('laser_scan_node')

def callback(msg):
  
  print msg.ranges[360]
  move.Float32 = 1.0
  if msg.ranges[360] < 2 :
    move.Flaot32 = 0
  pub.publish(move)

rospy.init_node('Check Obstacle')
sub = rospy.Subscriber('sim_ros_interface/front_scan', Laserscan , callback)
pub = rospy.Publisher('/Motor1Speed_youbot' , std_msgs)
move = std_msgs()
rospy.spin()




