#!/usr/bin/env python

import numpy as np
import math
import time

import rospy
import time

try:
    from ControlVRep import vrep  # run with rosnode 
except ImportError:
    import vrep     # run with python directly
else:
    print("Message from cubeRotatorLifterControl.py : import Vrep Success!")

def Start(IP='127.0.0.1', PORT=19998):# Local IP and API address (19999)
	# This fucntion starts the communication with the simulator
	vrep.simxFinish(-1) # Finish all the connections
	clientID=vrep.simxStart(IP, PORT, True, True, 5000, 5) # Start a new connection in the VREP default port 19999 
	while clientID == -1:
		clientID=vrep.simxStart(IP, PORT, True, True, 5000, 5) # Start a new connection in the VREP default port 19999 # Keep connecting if connection not established
		print("cubeRotatorLifterControl.py - Fail to connect VRep, reconnecting!")
		#rospy.set_param('ds_vrep_connected', False)
		time.sleep(.005)
	print("cubeRotatorLifterControl.py - Connection stablished with VRep")
	#rospy.set_param('ds_vrep_connected', True)
	return clientID
