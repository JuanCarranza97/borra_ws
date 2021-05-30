#!/usr/bin/env python
import rospy
from beginner_tutorials.msg import IoTSensor
from time import sleep

def iot_talker():
    publisher = rospy.Publisher("iot_line", IoTSensor, queue_size=10)
    rospy.init_node("iot_sensor")
    sensor = IoTSensor()
    while not rospy.is_shutdown():
        sensor.id = 123
        sensor.name = "Outdor 1"
        sensor.temperature = 20.23
        sensor.humidity = 99.43
        publisher.publish(sensor)
        rospy.loginfo("IoTSensor: \n%s"%sensor)
        sleep(.5)

if __name__ == "__main__":
    try:
        iot_talker()
    except rospy.ROSInterruptException:
        pass
