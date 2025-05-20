import numpy as np
import cv2, PIL
from cv2 import aruco
import matplotlib.pyplot as plt
import matplotlib as mpl
# import pandas as pd

vid = cv2.VideoCapture(0)

while (True):

    ret, frame = vid.read()
    #cv2.imshow('frame', frame)
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
    parameters =  cv2.aruco.DetectorParameters()
    detector = cv2.aruco.ArucoDetector(aruco_dict, parameters)
    markerCorners, markerIDs, rejectedImgPoints = detector.detectMarkers(frame)
    frame_markers = aruco.drawDetectedMarkers(frame.copy(), markerCorners, markerIDs)

    print(markerIDs)
    cv2.imshow("frame", frame_markers)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        # Destroy all the windows
        cv2.destroyAllWindows()
        break
vid.release()    
    
