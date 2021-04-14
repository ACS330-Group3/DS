# DS

Cmd environment for ROS master control:

# Steps

1. open VRep
cd ~/Downloads/V-REP_PRO_EDU_V3_6_1_Ubuntu18_04/
./vrep.sh
File > Open Scene > located "ABB140_Draws_Cube01.ttt" > press run

2. using roslaunch for launching ds node
roslaunch ud_bringup ds_system.launch

or

2.1. roscore
rosparam set ds_Reset False
rosparam set ds_robot_arm_EmergencyS False
rosparam set ds_robot_arm_drawing False
rosparam set ds_vrep_connected False
rosparam set ds_C_ID "107"
rosparam set ds_PicG "450"
rosparam set ds_ud_Location "notReceived"

2.2. run the python drawing code
rosrun ds_robot_arm_pkg ros_abb140control.py

2.3. run the python robot arm drawing server code
rosrun ds_robot_arm_pkg ros_abb140control_ser.py 

2.4. run the python emergency_action.py
rosrun ds_emergency_pkg emergency_action.py

2.5. run the python ds_pic_retrive.py
rosrun ds_master_cs ds_pic_retrive.py

2.6. run the python ds_ros_master.py
rosrun ds_master_cs ds_ros_master.py

2.7. run the python ds_cube_lifter.py
rosrun ds_master_cs ds_cube_lifter.py

2.8. run the python ds_cube_rotator.py
rosrun ds_master_cs ds_cube_rotator.py

2.9. run the python ds_cube_locator_ser.py
rosrun ds_visual_system_pkg ds_cube_locator_ser.py

3. print out all the rosinfo
rostopic echo /rosout

4. send fake RFID ID
rostopic pub /ds_cube_sensed ud_msgs/CubeLifterMessagePkg "{udiceReceived: true, udiceWeight: 0.0, ds_Cube_ID: 'sky'}" 







