#include <ros/ros.h>
#include <std_msgs/Int32.h>
#include <std_msgs/String.h>

void carCountCallback(const std_msgs::Int32::ConstPtr& msg)
{
    // Determine traffic light status based on car count
    std_msgs::String light_msg;
    if (msg->data > 0)
    {
        light_msg.data = "red";
    }
    else
    {
        light_msg.data = "green";
    }

    ROS_INFO("Traffic light status: %s", light_msg.data.c_str());
}

int main(int argc, char** argv)
{
    ros::init(argc, argv, "traffic_light_controller");
    ros::NodeHandle nh;

    ros::Subscriber car_count_sub = nh.subscribe("car_count", 10, carCountCallback);

    ros::spin();

    return 0;
}

