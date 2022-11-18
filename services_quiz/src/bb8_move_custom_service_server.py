#! /usr/bin/env python
import rospy

# you import the service message python classes generated from Empty.srv.
from geometry_msgs.msg import Twist
from services_quiz.srv import *

pub = rospy.Publisher('/cmd_vel',
                      Twist, queue_size=10)
var = Twist()


def my_callback(request):
    d = rospy.Duration(1.85, 0)
    for i in range(request.repetitions):
        print("Repeticion {}".format(i+1))
        for _ in range(4):
            var.linear.x = 0.5
            var.angular.z = 0
            pub.publish(var)
            rospy.sleep(request.side)

            var.linear.x = 0
            var.angular.z = 1
            pub.publish(var)
            rospy.sleep(d)
    var.linear.x = 0
    var.angular.z = 0
    pub.publish(var)

    print("Fin")

    response = BB8CustomServiceMessageResponse()
    response.success = True
    return response


rospy.init_node('service_server')
# create the Service called my_service with the defined callback
my_service = rospy.Service(
    '/move_bb8_in_square_custom', BB8CustomServiceMessage, my_callback)
rospy.spin()  # maintain the service open.
