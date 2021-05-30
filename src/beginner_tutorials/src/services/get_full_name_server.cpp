#include "ros/ros.h"
#include "beginner_tutorials/GetFullName.h"
#include <sstream>

bool append_name(beginner_tutorials::GetFullName::Request &req,
                 beginner_tutorials::GetFullName::Response &res);

int main(int argc, char **argv){
    ros::init(argc, argv, "get_full_name_server");
    ros::NodeHandle n;
    ros::ServiceServer service=n.advertiseService("get_full_name",append_name);
    ROS_INFO("Ready to append name");
    ros::spin();
}

bool append_name(beginner_tutorials::GetFullName::Request &req,
                 beginner_tutorials::GetFullName::Response &res){
    std::stringstream ss;
    //ss << req->name << " " req->last_name;
    ss << req.name << " " << req.last_name;
    res.full_name = ss.str();
    ROS_INFO("GetFullName - Name: %s, LastName: %s, - %s",req.name.c_str(), req.last_name.c_str(),res.full_name.c_str());
    return true;
}
