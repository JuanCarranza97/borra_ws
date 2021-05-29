#include "ros/ros.h"
#include "geometry_msgs/Twist.h"

int main(int argc, char **argv){
    ros::init(argc, argv, "turtle_mover");
    ros::NodeHandle n;
    ros::Publisher publisher=n.advertise<geometry_msgs::Twist>("/turtle1/cmd_vel",1000);
    ros::Rate loop_rate(2);
    while (ros::ok()){
        geometry_msgs::Twist twist;
        twist.linear.x = 1.0;
        twist.angular.z = 1.5;
        publisher.publish(twist);
        ros::spinOnce();
        loop_rate.sleep();
    }
    return 0;
}
