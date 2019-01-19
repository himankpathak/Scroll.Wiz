
import sys
import cv2
import os
from sys import platform
import argparse
import numpy as np
import pyautogui

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
parser.add_argument("--image_path", default="../../../examples/media/COCO_val2014_000000000192.jpg", help="Process an image. Read all standard formats (jpg, png, bmp, etc.).")
args = parser.parse_known_args()

# Custom Params
params = dict()
params["disable_multi_thread"] = False
# params["camera_resolution"] = "-1x-1"
params["model_folder"] = "/media/himank/Himank/Projects/LinuxProg/openpose/models/"
# params["output_resolution"] = "-1x-1"
# params["net_resolution"] = "128x128"
# params["hand_net_resolution"] = "368x368"
# params["hand_scale_number"] = 6
# params["hand_tracking"] = True
# params["process_real_time"] = True
params["hand"] = True
# params["body_disable"] = True
params["number_people_max"] = 1
params["hand_render_threshold"] = 0.2


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

def pressme(button,dir):
    try:
        if(button==2 and dir>0):
            pyautogui.scroll(4)
            print("scrolling up")
        elif(button==2 and dir<0):
            pyautogui.scroll(-4)
            print("scrolling down")
    except:
        pass

def coord(p1,p2):
    try:
        # print(abs(datum.handKeypoints[1][0][p1][0]-datum.handKeypoints[1][0][p2][0])+abs(datum.handKeypoints[1][0][p1][1]-datum.handKeypoints[1][0][p2][1]))
        # print((((datum.handKeypoints[1][0][p1][0]-datum.handKeypoints[1][0][p2][0])**2) + ((datum.handKeypoints[1][0][p1][1]-datum.handKeypoints[1][0][p2][1])**2))**0.5)
        if(datum.handKeypoints[1][0][p1][2]!=0 and (abs(datum.handKeypoints[1][0][p1][0]-datum.handKeypoints[1][0][p2][0]) + abs(datum.handKeypoints[1][0][p1][1]-datum.handKeypoints[1][0][p2][1]))<30):
            print("hello")
            return 1
        elif(flagmid>1 and datum.handKeypoints[1][0][p1][2]!=0 and (abs(datum.handKeypoints[1][0][p1][0]-datum.handKeypoints[1][0][p2][0]) + abs(datum.handKeypoints[1][0][p1][1]-datum.handKeypoints[1][0][p2][1]))>60):
            print("no hello")
            return -1
        else:
            return 0
    except:
        return 0

flagmid=0
# Process Image
datum = op.Datum()
cap = cv2.VideoCapture(0)
while True:
    blank,imageToProcess=cap.read()
    imageToProcess = cv2.flip(imageToProcess,1)
    datum.cvInputData = imageToProcess
    opWrapper.emplaceAndPop([datum])

    # Display Image Points
    # print("Body keypoints: \n" + str(datum.poseKeypoints))
    # print("Left hand keypoints: \n" + str(datum.handKeypoints[0]))
    # print("Right hand keypoints: \n" + str(datum.handKeypoints[1]))
    # while 1:
    if(flagmid<3):
        flagmid+=coord(4,12)
        n=1
    elif(n==1):
        n=0
        temp=datum.handKeypoints[1][0][4][1]
        pressme(2,datum.handKeypoints[1][0][4][1]-temp)
    else:
        if(datum.handKeypoints[1][0][4][2]==0 or (abs(datum.handKeypoints[1][0][4][0]-datum.handKeypoints[1][0][12][0]) + abs(datum.handKeypoints[1][0][4][1]-datum.handKeypoints[1][0][12][1]) )>70):
            print("no hello")
            flagmid=0
        pressme(2,datum.handKeypoints[1][0][4][1]-temp)

    # print(str(datum.poseKeypoints[0][4]))

    cv2.imshow("win", datum.cvOutputData)
    cv2.waitKey(1)
