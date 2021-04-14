#!/usr/bin/env python

import sys 
import os
import numpy as np
import rospy

from ud_msgs.srv import dsCLiftsrv

def CLiftSerHandle(req):
	if str(req.CLiftDirection) == 'up':
		rospy.loginfo("CLift service request received : up")
		# lift function for VRep - check parameter with /ds_robot_arm_EmergencyS is false
		rospy.loginfo("CLift service provided : up")
		cubeLocation = 'CubeRotator'
		rospy.loginfo("CL is : {}".format(cubeLocation))
		rospy.set_param('ds_ud_Location', cubeLocation)
		return True
	elif str(req.CLiftDirection) == 'down':
		rospy.loginfo("CLift service request received : down")
		# lift function for VRep - check parameter with /ds_robot_arm_EmergencyS is false
		rospy.loginfo("CLift service provided : down")
		cubeLocation = 'CubeLifter'
		rospy.loginfo("CL is : {}".format(cubeLocation))
		rospy.set_param('ds_ud_Location', cubeLocation)
		return True
	return False

if __name__ == "__main__":
	rospy.init_node("ds_cube_lifter_server")
	rospy.loginfo("ds_cube_lifter_server node created")

	service = rospy.Service("/ds_CLift_ser", dsCLiftsrv, CLiftSerHandle)

	rospy.loginfo("ds_cube_lifter_server service READY")

	rospy.spin()
