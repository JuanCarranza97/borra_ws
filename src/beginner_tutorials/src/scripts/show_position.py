#!/usr/bin/env python
import rospy
from turtlesim.msg import Pose

def turtle_pose_callback(message):
    x = message.x
    y = message.y
    rospy.loginfo("Turtle Position - x: %.2f, y: %.2f"%(x,y))

def pose_listener():
    rospy.init_node("pose_listener")
    rospy.Subscriber("/turtle1/pose", Pose, turtle_pose_callback)
    rospy.spin()

if __name__ == "__main__":
    pose_listener()
