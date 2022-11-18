#! /usr/bin/env python
import rospy
import actionlib
from actions_quiz.msg import CustomActionMsgFeedback, CustomActionMsgResult, CustomActionMsgAction
from geometry_msgs.msg import Pose
from std_msgs.msg import Empty


class CustomActionClass(object):

    # create messages that are used to publish feedback/result
    _feedback = CustomActionMsgFeedback()
    _result = CustomActionMsgResult()

    _take_off_publisher = None
    _land_publisher = None
    _actual_pose = Pose()

    def __init__(self):
        rospy.Subscriber('/drone/gt_pose', Pose, self.gt_pose_callback)
        self._take_off_publisher = rospy.Publisher(
            "/drone/takeoff", Empty, queue_size=10)
        self._land_publisher = rospy.Publisher(
            "/drone/land", Empty, queue_size=10)

        # creates the action server
        self._as = actionlib.SimpleActionServer(
            "action_custom_msg_as", CustomActionMsgAction, self.goal_callback, False)
        self._as.start()

    def gt_pose_callback(self, msg):
        print(msg.position.z)
        self._actual_pose = msg

    def goal_callback(self, goal):
        r = rospy.Rate(1)
        success = False

        if goal.goal == "TAKEOFF":
            self._feedback.feedback = "taking off"
            self._take_off_publisher.publish()
            while self._actual_pose.position.z < 1.0:
                self._as.publish_feedback(self._feedback)
                r.sleep()
            success = True
        elif goal.goal == "LAND":
            self._feedback.feedback = "landing"
            self._land_publisher.publish()
            while self._actual_pose.position.z > 1.0:
                self._as.publish_feedback(self._feedback)
                r.sleep()
            success = True

        if success:
            rospy.loginfo(
                'Succeeded ')
            self._as.set_succeeded(self._result)


if __name__ == '__main__':
    rospy.init_node('actions_quiz')
    CustomActionClass()
    rospy.spin()
