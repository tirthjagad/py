#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Float32
rospy.init_node('laser_scan_node')

def callback(msg):
  
  print msg.ranges[360]
  move = -1.0
  move1 = -1.0
  move2 = -1.0
  move3 = -1.0
  if msg.ranges[360] < 1 :
    move = 1.0
    move1 = 1.0
    move2 = -1.0
    move3 = -1.0
  pub.publish(move)
  pub1.publish(move1)
  pub2.publish(move2)
  pub3.publish(move3)


sub = rospy.Subscriber('sim_ros_interface/front_scan', LaserScan , callback)
pub = rospy.Publisher('/Motor1Speed_youbot' , Float32 , queue_size=50)
pub1 = rospy.Publisher('/Motor2Speed_youbot' , Float32 , queue_size=50)
pub2 = rospy.Publisher('/Motor3Speed_youbot' , Float32 , queue_size=50)
pub3 = rospy.Publisher('/Motor4Speed_youbot' , Float32 , queue_size=50)
move=Float32
move1=Float32
move2=Float32
move3=Float32
rospy.spin()





