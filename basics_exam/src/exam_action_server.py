#! /usr/bin/env python
import rospy
import actionlib
from basics_exam.msg import record_odomResult, record_odomAction
from geometry_msgs.msg import Pose
from nav_msgs.msg import Odometry
from std_msgs.msg import Empty


class CustomActionClass(object):

    # create messages that are used to publish feedback/result
    _result = record_odomResult()
    _record_odom = False

    def __init__(self):
        rospy.Subscriber('/odometry/filtered', Odometry, self.odom_callback)

        # creates the action server
        self._as = actionlib.SimpleActionServer(
            "rec_odom_as", record_odomAction, self.goal_callback, False)
        self._as.start()

    def odom_callback(self, msg):
        if(self._record_odom):
            self._result.result.extend(msg.pose.pose)

    def goal_callback(self, goal):
        rospy.loginfo('Recording odom pose ')
        self._record_odom = True
        rospy.sleep(60)
        self._record_odom = False
        self._as.set_succeeded(self._result)
        self._result.result = []


if __name__ == '__main__':
    rospy.init_node('exam_action_server')
    CustomActionClass()
    rospy.spin()
