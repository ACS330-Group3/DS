#!/usr/bin/env python

import sys 
import os
import numpy as np
import rospy

from std_msgs.msg import Bool
from ud_msgs.msg import PicInfoMessagePkg

def pic_retrieve_ProcessStart(req):
	if req.data == True:
		rospy.loginfo("ds_pic_retrieve.py - pic retrieve request received")
		pub1.publish(True,'sky',"600")
		

if __name__ == "__main__":
	rospy.init_node("ds_pic_retrieve_service")
	rospy.loginfo("ds_pic_retrieve_service node created")

	sub1 = rospy.Subscriber("/ds_pic_retrieve_ProcessStart", Bool, pic_retrieve_ProcessStart)

	pub1 = rospy.Publisher("/ds_pic_retrieved",PicInfoMessagePkg,queue_size=10)

	rospy.spin()
