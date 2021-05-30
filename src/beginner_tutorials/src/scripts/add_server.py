#!/usr/bin/env python
import rospy
from beginner_tutorials.srv import AddTwoInts
#from beginner_tutorials.srv import AddTwoIntsRequest
from beginner_tutorials.srv import AddTwoIntsResponse

def handle_add_two_ints(req):
    sum_value = req.a + req.b
    rospy.loginfo("Return values [%d + %d = %d]"%(req.a, req.b, sum_value))
    if req.a > 10:
        rospy.logwarn("A is greater than 10!!!")
    return AddTwoIntsResponse(sum_value)

def add_two_ints_server():
    rospy.init_node("add_two_ints_server")
    s = rospy.Service(
        "add_two_ints",      #Service name
        AddTwoInts,          #Service type
        handle_add_two_ints) #Callback function
    rospy.loginfo("Ready to add two ints")
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()

