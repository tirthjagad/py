#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan

rospy.init_node('laser_scan_publisher')

scan_pub = rospy.Publisher('sim_ros_interface/front_scan', LaserScan, queue_size=50)

num_readings = 100
laser_frequency = 40

count = 0
r = rospy.Rate(1.0)
while not rospy.is_shutdown():
    current_time = rospy.Time.now()

    sim_ros_interface/front_scan = LaserScan()

    sim_ros_interface/front_scan.header.stamp = current_time
    sim_ros_interface/front_scan.header.frame_id = 'laser_frame'
    sim_ros_interface/front_scan.angle_min = -1.57
    sim_ros_interface/front_scan.angle_max = 1.57
    sim_ros_interface/front_scan.angle_increment = 3.14 / num_readings
    sim_ros_interface/front_scan.time_increment = (1.0 / laser_frequency) / (num_readings)
    sim_ros_interface/front_scan.range_min = 0.0
    sim_ros_interface/front_scan.range_max = 100.0

    sim_ros_interface/front_scan.ranges = []
    sim_ros_interface/front_scan.intensities = []
    for i in range(0, num_readings):
        sim_ros_interface/front_scan.ranges.append(1.0 * count)  # fake data
        sim_ros_interface/front_scan.intensities.append(1)  # fake data

    scan_pub.publish(sim_ros_interface/front_scan)
    count += 1
    r.sleep()
