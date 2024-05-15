#include <ros/ros.h>
#include <geometry_msgs/Twist.h>
#include <nav_msgs/Odometry.h>

int main(int argc, char **argv){
    ros::init(argc, argv, "main_node");
    ros::NodeHandle nh;
    ROS_INFO("In CPP Main Node");
}