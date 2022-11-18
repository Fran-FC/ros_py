#! /usr/bin/env python
import rospy

from services_quiz.srv import *

rospy.init_node('service_client')

rospy.wait_for_service('move_bb8_in_square_custom')
try:
    bb8_move = rospy.ServiceProxy(
        "move_bb8_in_square_custom", BB8CustomServiceMessage)
    resp = bb8_move(2, 2)
    resp = bb8_move(4, 1)
except rospy.ServiceException as e:
    print("Service call failed: %s" % e)

rospy.spin()  # maintain the service open.
