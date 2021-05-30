#!/usr/bin/env python
import sys
import rospy
from beginner_tutorials.srv import AddTwoInts
#from beginner_tutorials.srv import AddTwoIntsRequest
#from beginner_tutorials.srv import AddTwoIntsResponse

def add_two_ints_client(x, y):
    rospy.wait_for_service("add_two_ints") #Wait for service to be enable
    try:
        add_two_ints = rospy.ServiceProxy(
            "add_two_ints", #Server name
            AddTwoInts)     #Server type
        resp1 = add_two_ints(x, y)
        return resp1.sum
    except rospy.ServiceException(e):
        print("Service call failed: %s"%e)

if __name__ == "__main__":
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        print("Check usage!!")
        sys.exit(1)
    print("Requesting %s+%s"%(x, y))
    s = add_two_ints_client(x, y)
    print("  RESULT - %s + %s = %s"%(x, y, s))
    sys.exit(0)
