#!/usr/bin/env python
import rospy
from beginner_tutorials.msg import IoTSensor

def get_sensor_values(message):
    sensor_id = message.id
    sensor_name = message.name
    temperature = message.temperature
    humidity    = message.humidity
    rospy.loginfo(" %s (%d) - Temperature: %.2f Humidity: %.2f"%(
        sensor_name, sensor_id, temperature, humidity))

def listener():
    rospy.init_node("iot_listener")
    rospy.loginfo("IoT Listener initialized")
    rospy.Subscriber("iot_line", IoTSensor, get_sensor_values)
    rospy.spin()

if __name__ == "__main__":
    listener()
