#!/usr/bin/env python

import sys 
import os
import numpy as np
import rospy

from ud_msgs.srv import dsCRotatesrv

def CRotateSerHandle(req):
	if req.imgRequestPosition == 0: # rotate
		rospy.loginfo("CRotate service request received : 0 position")
		# rotate function for VRep - check parameter with /ds_robot_arm_EmergencyS is false
		rospy.loginfo("CRotate service provided : to 1st position")
		return True	
	elif req.imgRequestPosition == 1: # grab
		rospy.loginfo("CRotate service request received : 1st position")
		# rotate function for VRep - check parameter with /ds_robot_arm_EmergencyS is false
		rospy.loginfo("CRotate service provided : cube is grabbed")
		return True		
	elif req.imgRequestPosition == 2: # rotate
		rospy.loginfo("CRotate service request received : 2nd position")
		# rotate function for VRep - check parameter with /ds_robot_arm_EmergencyS is false
		rospy.loginfo("CRotate service provided : 2nd position")
		return True	
	elif req.imgRequestPosition == 3: # rotate
		rospy.loginfo("CRotate service request received : 3rd position")
		# rotate function for VRep - check parameter with /ds_robot_arm_EmergencyS is false
		rospy.loginfo("CRotate service provided : 3rd position")
		return True	
	elif req.imgRequestPosition == 4: # rotate
		rospy.loginfo("CRotate service request received : 4th position")
		# rotate function for VRep - check parameter with /ds_robot_arm_EmergencyS is false
		rospy.loginfo("CRotate service provided : 4th position")
		return True	
	elif req.imgRequestPosition == 5: # rotate
		rospy.loginfo("CRotate service request received : 5th position")
		# rotate function for VRep - check parameter with /ds_robot_arm_EmergencyS is false
		rospy.loginfo("CRotate service provided : 5th position")
		return True	
	elif req.imgRequestPosition == 6: # rotate
		rospy.loginfo("CRotate service request received : 6th position")
		# rotate function for VRep - check parameter with /ds_robot_arm_EmergencyS is false
		rospy.loginfo("CRotate service provided : 6th position")
		return True	
	elif req.imgRequestPosition == 7: # release
		rospy.loginfo("CRotate service request received : 7th position")
		# rotate function for VRep - check parameter with /ds_robot_arm_EmergencyS is false
		rospy.loginfo("CRotate service provided : cube release")
		return True	
	return False

if __name__ == "__main__":
	rospy.init_node("ds_cube_rotate_server")
	rospy.loginfo("ds_cube_rotate_server node created")

	service = rospy.Service("/ds_CRotate_ser", dsCRotatesrv, CRotateSerHandle)

	rospy.loginfo("ds_cube_rotate_server service READY")

	rospy.spin()
