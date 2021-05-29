#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def chatter_callback(message):
    #caller_id = rospy.get_caller_id()
    data = message.data
    rospy.loginfo("I heard '%s'"%(data))

def listener():
    #Create listener node
    #rospy.init_node('listener', anonymous=True)
    rospy.init_node('listener')
    rospy.loginfo("Listener node initialized")
    #Create chatter topic of Type strings and chatter_callback as callback
    rospy.Subscriber("chatter", String, chatter_callback)
    rospy.loginfo("Chatter topic listening")
    rospy.spin()
    
if __name__ == "__main__":
    listener()

