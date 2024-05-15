#include <ros/ros.h>
#include <geometry_msgs/Twist.h>
#include <nav_msgs/Odometry.h>

nav_msgs::Odometry robotOdom;
void odomCb(const nav_msgs::Odometry::ConstPtr& msg){
    robotOdom = *msg;
}

int main(int argc, char **argv){
    ros::init(argc, argv, "main_node");
    ros::NodeHandle nh;
    ROS_INFO("In CPP Main Node");

    ros::Subscriber state_sub = nh.subscribe<nav_msgs::Odometry>
            ("/warthog_velocity_controller/odom", 10, odomCb);

    // use this to send Twists that would move the robot.
    ros::Publisher cmdVelPub = nh.advertise<geometry_msgs::Twist>
        ("/warthog_velocity_controller/cmd_vel", 10);

    ros::Rate rate(20.0);

    while (ros::ok())
    {
        ros::spinOnce();
        rate.sleep();
    }
    
}