#include "ros/ros.h"
#include "beginner_tutorials/GetFullName.h"
#include <cstdlib>

int main(int argc, char **argv){
    ros::init(argc, argv, "get_full_name_client");
    if (argc != 3){
        ROS_WARN("Usage: add_two_ints_client x y");
        return 1;
    }
    ros::NodeHandle n;
    ros::ServiceClient client = n.serviceClient<beginner_tutorials::GetFullName>("get_full_name");
    beginner_tutorials::GetFullName srv;
    srv.request.name = argv[1];
    srv.request.last_name = argv[2];
    if (client.call(srv)){
        ROS_INFO("Full Name: %s", srv.response.full_name.c_str());
    }
    else{
        return 1;
    }
    return 0;
}
