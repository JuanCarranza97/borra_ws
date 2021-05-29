#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from time import sleep 

def talker():
    #Create publisher topic
    #  Name: chatter
    #  Type: String
    #  queue_size=10
    publisher = rospy.Publisher('chatter', String, queue_size=10)  
    #Create 'talker' node
    #anonymous=True flag means rospy will chose
    # a unique name for out 'talker' node
    #rospy.init_node('talker',anonymous=True) 
    rospy.init_node('talker') 
    i = 0
    while not rospy.is_shutdown():
        hello_str = "Hello world!!! [%s]"%i
        rospy.loginfo(hello_str)
        publisher.publish(hello_str)
        sleep(.5)
        i+=1

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        print("Closing ROS!!!")

