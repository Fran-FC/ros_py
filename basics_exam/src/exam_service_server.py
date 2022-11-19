#! /usr/bin/env python
import rospy

# you import the service message python classes generated from Empty.srv.
# from geometry_msgs.msg import Twist
from std_srvs.srv import Trigger, TriggerResponse
from sensor_msgs.msg import LaserScan


resp = ""


def scan_callback(msg):
    global resp

    center = int(len(msg.ranges) / 2)
    right = 20
    left = len(msg.ranges) - 21
    points = [
        msg.ranges[center],
        msg.ranges[left],
        msg.ranges[right]
    ]
    closest = 1000.0
    for p in points:
        if p < closest:
            closest = p

    if msg.ranges[center] == closest:
        resp = "center"
    elif msg.ranges[left] == closest:
        resp = "left"
    elif msg.ranges[right] == closest:
        resp = "right"


def service_callback(req):
    response = TriggerResponse(success=True,
                               message=resp)
    return response


sub = rospy.Subscriber("/scan", LaserScan, scan_callback)

# create the Service called my_service with the defined callback
my_service = rospy.Service(
    '/crash_direction_service', Trigger, service_callback)

rospy.init_node('exam_service_server')

rospy.spin()  # maintain the service open.
