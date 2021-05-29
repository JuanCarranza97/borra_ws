#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from time import sleep

def turtle_mover():
    publisher = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    rospy.init_node("turtle_mover")
    twist = Twist()
    while not rospy.is_shutdown():
        twist.linear.x  = 1.0
        twist.angular.z = 1.5
        rospy.loginfo("Moving turtle:\n%s"%(twist))
        publisher.publish(twist)
        sleep(.5)

if __name__ == "__main__":
    try:
        turtle_mover()
    except rospy.ROSInterruptException:
        pass
