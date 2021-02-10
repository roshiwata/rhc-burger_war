#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Publish my position from TF 
import roslib
import rospy
import tf2_ros
import tf_conversions
import tf
import math 
from geometry_msgs.msg import PoseStamped 
from geometry_msgs.msg import Quaternion

class PubEnemyPose():

    def __init__(self):
        #Get parameter
        self.rate = rospy.get_param("~rate", 1)
        #self.side = rospy.get_param("~side", "r")

        #Transformer, Listener, Subscriber, Publisher
        self.tfBuffer = tf2_ros.Buffer()
        self.listener = tf2_ros.TransformListener(self.tfBuffer)
        self.my_pub = rospy.Publisher('my_pose', PoseStamped, queue_size=10)

        #Initilize
        self.my_ps = PoseStamped()

    def lis_pub_my_ps(self):
        rate = rospy.Rate(self.rate)

        msg = PoseStamped()
        msg.header.frame_id = "map"
        while not rospy.is_shutdown():
            try:
                t = self.tfBuffer.lookup_transform('map', 'base_footprint', rospy.Time(0), rospy.Duration(1.0))
            except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
                #rospy.logerr('LookupTransform Eroor my pose !')
                rate.sleep()
                continue
            self.my_ps.pose.position = t.transform.translation
            self.my_ps.pose.orientation = t.transform.rotation
            msg.pose = self.my_ps.pose
            self.my_pub.publish(msg)
            rate.sleep()

if __name__ == '__main__':
    rospy.init_node('pub_my_pose')
    pub_self = PubEnemyPose()
    try:
        pub_self.lis_pub_my_ps()

    except rospy.ROSInterruptException: pass