#include "ros/ros.h"
#include "std_msgs/String.h"
#include <sstream>

int main(int argc, char **argv){
    //Initialize ROS node name "talker"
    ros::init(argc, argv, "talker_node"); 
    //Create a new node 
    ros::NodeHandle n;
    //Create publisher with a topic "chatter"
    // Name: chatter
    // Type str_msgs/String
    ros::Publisher chatter_publisher = n.advertise<std_msgs::String>("chatter", 1000);
    //Rate to define frequency for a loop
    ros::Rate loop_rate(2);
    int count = 0;
    while (ros::ok()) {
        //Create a new String ROS message
        std_msgs::String msg;
        //Create a string for the data
        std::stringstream ss;
        ss << "Hello world!!!! C++ " << count;
        msg.data = ss.str();
        ROS_INFO("[C++ Talker] I published %s", msg.data.c_str());
        chatter_publisher.publish(msg);
        ros::spinOnce(); //Need to call this function to allow ROS process incoming
        loop_rate.sleep();
        count++;
    }
    return 0;
}
