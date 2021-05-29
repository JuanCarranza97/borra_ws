#include "ros/ros.h"
#include "turtlesim/Pose.h"

void turtle_pose_callback(const turtlesim::Pose::ConstPtr& msg);

int main(int argc, char **argv){
    ros::init(argc, argv, "pose_listener");
    ros::NodeHandle n;
    ros::Subscriber sub = n.subscribe("/turtle1/pose", 1000, turtle_pose_callback);
    ros::spin();
}

void turtle_pose_callback(const turtlesim::Pose::ConstPtr& msg){
    ROS_INFO("Turtle Position - X: %.2f, Y: %.2f",msg->x, msg->y);   
    if ( (msg->x < 1.0) && (msg->y < 1.0)) {
        ROS_WARN("Turtle is near 0,0");
    }
}
