import cv2
from cv2 import aruco
import matplotlib.pyplot as plt
import urllib.request
import numpy as np
import concurrent.futures
import socket

 
url= 'http://192.168.43.147/cam-lo.jpg'
im=None
 
def run1():
    cv2.namedWindow("live transmission", cv2.WINDOW_AUTOSIZE)
    while True:

        img_resp=urllib.request.urlopen(url)
        imgnp=np.array(bytearray(img_resp.read()),dtype=np.uint8)
        im = cv2.imdecode(imgnp,-1)

        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
        parameters =  cv2.aruco.DetectorParameters()
        detector = cv2.aruco.ArucoDetector(aruco_dict, parameters)
        markerCorners, markerIDs, rejectedImgPoints = detector.detectMarkers(im)
        frame_markers = aruco.drawDetectedMarkers(im.copy(), markerCorners, markerIDs)
        if markerIDs is not None:
            for i in range(len(markerIDs)):
                if markerIDs[i] == targetid:  # Check if the detected marker has ID 1
                    aruco.drawDetectedMarkers(im, markerCorners, markerIDs)


        cv2.imshow('live transmission',frame_markers)
        key=cv2.waitKey(5)
        if key==ord('q'):
            break
            
    cv2.destroyAllWindows()
    
targetid = 1
 
if __name__ == '__main__':
    print("started")
    with concurrent.futures.ProcessPoolExecutor() as executer:
            f1= executer.submit(run1)
        