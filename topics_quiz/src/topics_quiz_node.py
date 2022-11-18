#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

pub = rospy.Publisher('/cmd_vel',
                      Twist, queue_size=10)


def scan_callback(msg):
    center = int(len(msg.ranges) / 2)
    right = 20
    left = len(msg.ranges) - 21

    twist_msg = Twist()
    if msg.ranges[center] > 1.0:
        twist_msg.linear.x = 0.4
    else:
        twist_msg.angular.z = 0.4

    if msg.ranges[left] < 1.0:
        twist_msg.angular.z = -0.4
    if msg.ranges[right] < 1.0:
        twist_msg.angular.z = 0.4

    pub.publish(twist_msg)


rospy.init_node('topics_quiz_node')
sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, scan_callback)

rospy.spin()
