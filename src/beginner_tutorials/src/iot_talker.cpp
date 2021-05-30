#include "ros/ros.h"
#include "beginner_tutorials/IoTSensor.h"

int main(int argc, char **argv){
    ros::init(argc, argv, "iot_talker");        
    ros::NodeHandle n;
    ros::Publisher iot_publisher = n.advertise<beginner_tutorials::IoTSensor>("iot_line",1000);
    ros::Rate loop_rate(2);
    beginner_tutorials::IoTSensor iot_sensor;
    while (ros::ok()){
        iot_sensor.id = 457;
        iot_sensor.name = "Indor 2";
        iot_sensor.temperature = 23.20;
        iot_sensor.humidity = 43.99;
        iot_publisher.publish(iot_sensor);
        ROS_INFO("Message sent!!! %s", iot_sensor.name.c_str());
        ros::spinOnce();
        loop_rate.sleep();
    }
    return 0;
}
