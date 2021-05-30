#include "ros/ros.h"
#include "beginner_tutorials/IoTSensor.h"

void iot_sensor_callback(const beginner_tutorials::IoTSensor::ConstPtr& msg);

int main(int argc, char **argv){
    ros::init(argc, argv, "iot_listener");
    ros::NodeHandle n;
    ros::Subscriber sub = n.subscribe("iot_line", 1000, iot_sensor_callback);
    ros::spin();
    return 0;
}

void iot_sensor_callback(const beginner_tutorials::IoTSensor::ConstPtr& msg){
    ROS_INFO("[IoTSensor::%s (%d)] - Temperature: %.2f, Humidity: %.2f",
        msg->name.c_str(), msg->id, msg->temperature, msg->humidity);
}
