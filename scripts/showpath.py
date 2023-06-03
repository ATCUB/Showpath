#!/usr/bin/env python
#coding = UTF-8
from nav_msgs.msg import Path 
from geometry_msgs.msg import PoseStamped
import rospy

def callback( msg):
    my_poses = PoseStamped()
    #my_poses.pose.position.x
    for i in range(len(msg.poses)):
        my_poses = msg.poses[i]
        rospy.loginfo("%ird : x:%0.3f, y:%0.3f",i, my_poses.pose.position.x, my_poses.pose.position.y)
    #rospy.loginfo("Turtle pose: x:%0.3f, y:%0.3f", msg.x, msg.y)

def subscriber_plan():
       rospy.init_node('Showpath', anonymous=False)#init
       rospy.Subscriber("/move_base/NavfnROS/plan", Path,callback)
      # print("im here2!\r\n")

if __name__ == '__main__':
    #rospy.loginfo("hello_world")
    subscriber_plan()
    rospy.spin()
    #print("Im here!\r\n")

