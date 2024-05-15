#!/usr/bin/env python
from typing import Any
import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

class Node:
    """"""
    def __init__(self) -> None:
        """"""
        self.cmd_vel_pub = None
        self.robot_odom = None
        self.loop_rate = 5 # in hertz (AKA cycles per second)

        self.init_publishers()
        self.init_subscribers()


    def init_publishers(self):
        """"""
        rospy.loginfo("Initializing publishers.")
        self.cmd_vel_pub = rospy.Publisher("/warthog_velocity_controller/cmd_vel", Twist, queue_size=10)
        rospy.sleep(2)

    def init_subscribers(self):
        """
        Get robot location.
        """
        rospy.loginfo("Initializing subscribers.")
        rospy.Subscriber("/warthog_velocity_controller/odom", Odometry, self.get_robot_odom)

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        """"""
        # rate = rospy.Rate(1)
        # while len(self.signals) == 0 and len(self.vectors) == 0 and len(self.points) == 0:
        #     print("waiting for parameters")
        #     rate.sleep()
        # self.main_loop()
        rospy.spin()
    
    def get_robot_odom(self, message):
        """
        message
            pose
                pose
                    position
                        x
                        y
                        z
                    orientation
        """
        self.robot_odom = message
    
    def main_loop(self):
        rate = rospy.Rate(self.loop_rate)
        while not rospy.is_shutdown():
            # perform some action like publish cmd to move
            rate.sleep()



if __name__ == "__main__":
    rospy.init_node("aibr_node")
    rospy.loginfo("Initialized aibr_node")
    node = Node()
    node()