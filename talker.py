#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan

rospy.init_node('laser_scan_publisher')

scan_pub = rospy.Publisher('message_data', LaserScan, queue_size=50)

num_readings = 100
laser_frequency = 40

count = 0
r = rospy.Rate(1.0)
while not rospy.is_shutdown():
    current_time = rospy.Time.now()

    message_data = LaserScan()

    message_data.header.stamp = current_time
    message_data.header.frame_id = 'laser_frame'
    message_data.angle_min = -1.57
    message_data.angle_max = 1.57
    message_data.angle_increment = 3.14 / num_readings
    message_data.time_increment = (1.0 / laser_frequency) / (num_readings)
    message_data.range_min = 0.0
    message_data.range_max = 100.0

    message_data.ranges = []
    message_data.intensities = []
    for i in range(0, num_readings):
        message_data.ranges.append(1.0 * count)  # fake data
        message_data.intensities.append(1)  # fake data

    scan_pub.publish(sim_ros_interface/front_scan)
    count += 1
    r.sleep()
