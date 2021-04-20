#!/usr/bin/env python

import rospy
from ud_msgs.srv import csSendImages
from cv_bridge import CvBridge
import cv2
import os

dirname = os.path.dirname(__file__)
picfolder = os.path.join(dirname, "cs_image")

def imghandle(req):
	if req.requestID != '':
		requestID = str(req.requestID)
		IDPicName = '450'
		ImgList = []
		for PicNum in range(1,6+1): # included 1,2,3,4,5,6
			filename = requestID+'_'+IDPicName+'_'+str(PicNum)+'.png'
			filepath = os.path.join(picfolder, filename)
			image = cv2.imread(filepath)
			br = CvBridge()
			rospy.loginfo("Image of {} is sent!". format(filename))
			ImgList.append(br.cv2_to_imgmsg(image, encoding='passthrough'))
			#image1 = br.cv2_to_imgmsg(image, encoding='passthrough')
		#image1 = br.cv2_to_imgmsg(image)
		return IDPicName,ImgList[0],ImgList[1],ImgList[2],ImgList[3],ImgList[4],ImgList[5]
		
if __name__ == "__main__":
	rospy.init_node("CS_Img_Publish_Server")
	rospy.loginfo("CS_Img_Publish_Server node created")
	service = rospy.Service("/cs_image_service", csSendImages, imghandle)
	rospy.loginfo("CS_Img_Publish_Server server started")
	rospy.spin()
