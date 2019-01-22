
import sys
import cv2
import os
from sys import platform
import argparse
import numpy as np
import pyautogui

from popup import PopUp

dir_path = os.path.dirname(os.path.realpath(__file__))
try:
	if platform == "win32":
		sys.path.append(dir_path + '/../../python/openpose/Release');
		os.environ['PATH']  = os.environ['PATH'] + ';' + dir_path + '/../../x64/Release;' +  dir_path + '/../../bin;'
		import pyopenpose as op
	else:
		sys.path.append('../../python');
		from openpose import pyopenpose as op
except ImportError as e:
	print('Error: OpenPose library could not be found. Did you enable `BUILD_PYTHON` in CMake and have this Python script in the right folder?')
	raise e

# Flags
parser = argparse.ArgumentParser()
args = parser.parse_known_args()

# Custom Params
params = dict()
params["disable_multi_thread"] = False
# params["camera_resolution"] = "-1x-1"
params["model_folder"] = "/media/himank/Himank/Projects/LinuxProg/openpose/models/"
# params["output_resolution"] = "-1x-1"
params["net_resolution"] = "128x128"
# params["hand_net_resolution"] = "368x368"
# params["hand_scale_number"] = 6
# params["hand_tracking"] = True
# params["process_real_time"] = True
# params["hand"] = False
params["number_people_max"] = 1


# Add others in path
for i in range(0, len(args[1])):
	curr_item = args[1][i]
	if i != len(args[1])-1: next_item = args[1][i+1]
	else: next_item = "1"
	if "--" in curr_item and "--" in next_item:
		key = curr_item.replace('-','')
		if key not in params:  params[key] = "1"
	elif "--" in curr_item and "--" not in next_item:
		key = curr_item.replace('-','')
		if key not in params: params[key] = next_item

# Starting OpenPose
opWrapper = op.WrapperPython()
opWrapper.configure(params)
opWrapper.start()

def dist(p1,p2):
	return abs(datum.poseKeypoints[0][p1][0]-datum.poseKeypoints[0][p2][0])


# Process Image
datum = op.Datum()
cap = cv2.VideoCapture(0)
mode=1
flag=flag2=flag3=flag4=flag5=1
n=0

def changemode(m):
	if(m==1):
		return 2
	elif(m==2):
		return 3
	elif(m==3):
		return 1

while True:
	blank,imageToProcess=cap.read()
	imageToProcess = cv2.flip(imageToProcess,1)
	height,width = imageToProcess.shape[:2]
	datum.cvInputData = imageToProcess
	opWrapper.emplaceAndPop([datum])

	# Display Image Points
	# print("Body keypoints: \n" + str(datum.poseKeypoints))
	# print("Left hand keypoints: \n" + str(datum.handKeypoints[0]))
	# print("Right hand keypoints: \n" + str(datum.handKeypoints[1]))

	if(mode==1):
		# scroll content
		if(datum.poseKeypoints[0][4][1]==0):
			pass
		else:
			pyautogui.scroll(-(datum.poseKeypoints[0][4][1]-datum.poseKeypoints[0][2][1])/80)

		# change tabs
		if(datum.poseKeypoints[0][6][0]-datum.poseKeypoints[0][7][0]>100 and datum.poseKeypoints[0][7][0]!=0):
			if(flag2==1):
				flag2=0
				pyautogui.hotkey('ctrl','pageup')

		elif(datum.poseKeypoints[0][6][0]-datum.poseKeypoints[0][7][0]<-60 and datum.poseKeypoints[0][7][0]!=0):
			if(flag2==1):
				flag2=0
				pyautogui.hotkey('ctrl','pagedown')

		elif(datum.poseKeypoints[0][6][0]-datum.poseKeypoints[0][7][0]>-40 and datum.poseKeypoints[0][6][0]-datum.poseKeypoints[0][7][0]<40):
			flag2=1

	elif(mode==2):
		# print("YT MODE")

		# move 10 secs
		if(datum.poseKeypoints[0][6][0]-datum.poseKeypoints[0][7][0]>100 and datum.poseKeypoints[0][7][0]!=0):
			if(flag3==1):
				flag3=0
				pyautogui.press('j')

		elif(datum.poseKeypoints[0][6][0]-datum.poseKeypoints[0][7][0]<-60 and datum.poseKeypoints[0][7][0]!=0):
			if(flag3==1):
				flag3=0
				pyautogui.press('l')

		elif(datum.poseKeypoints[0][6][0]-datum.poseKeypoints[0][7][0]>-40 and datum.poseKeypoints[0][6][0]-datum.poseKeypoints[0][7][0]<40):
			flag3=1

		# play and full screen
		if(datum.poseKeypoints[0][4][1]-datum.poseKeypoints[0][4][1]>100 and datum.poseKeypoints[0][4][1]!=0):
			if(flag4==1):
				flag4=0
				pyautogui.press('k')

		elif(datum.poseKeypoints[0][3][1]-datum.poseKeypoints[0][4][1]<-60 and datum.poseKeypoints[0][4][1]!=0):
			if(flag4==1):
				flag4=0
				pyautogui.press('f')

		elif(datum.poseKeypoints[0][3][1]-datum.poseKeypoints[0][4][1]>-40 and datum.poseKeypoints[0][3][1]-datum.poseKeypoints[0][4][1]<40):
			flag4=1

	elif(mode==3):
		# print("YT MODE 2")

		# volume control
		if(datum.poseKeypoints[0][6][1]-datum.poseKeypoints[0][7][1]>100 and datum.poseKeypoints[0][7][1]!=0):
			if(flag5==1):
				flag5=0
				pyautogui.press('up')

		elif(datum.poseKeypoints[0][6][1]-datum.poseKeypoints[0][7][1]<-60 and datum.poseKeypoints[0][7][1]!=0):
			if(flag5==1):
				flag5=0
				pyautogui.press('down')

		elif(datum.poseKeypoints[0][6][1]-datum.poseKeypoints[0][7][1]>-40 and datum.poseKeypoints[0][6][1]-datum.poseKeypoints[0][7][1]<40):
			flag5=1

		# video playlist control
		if(datum.poseKeypoints[0][3][0]-datum.poseKeypoints[0][4][0]>100 and datum.poseKeypoints[0][4][0]!=0):
			if(flag==1):
				flag=0
				pyautogui.hotkey('shift','p')

		elif(datum.poseKeypoints[0][3][0]-datum.poseKeypoints[0][4][0]<-60 and datum.poseKeypoints[0][4][0]!=0):
			if(flag==1):
				flag=0
				pyautogui.hotkey('shift','n')

		elif(datum.poseKeypoints[0][3][0]-datum.poseKeypoints[0][4][0]>-40 and datum.poseKeypoints[0][3][0]-datum.poseKeypoints[0][4][0]<40):
			flag=1

	# elif(mode==4):
		# print("mODE 4")

	if(n>=1):
		n-=1
		# print (n)
	elif((datum.poseKeypoints[0][4][1]!=0 and n==0) and ((abs(datum.poseKeypoints[0][4][0]-datum.poseKeypoints[0][7][0]) + abs(datum.poseKeypoints[0][4][0]-datum.poseKeypoints[0][7][0])) <180)):
		n=20
		mode=changemode(mode)
		PopUp(mode-1);
		# print("yeaaa")

	cv2.imshow("window", datum.cvOutputData)
	cv2.waitKey(1)
