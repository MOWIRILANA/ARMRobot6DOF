import numpy as np
import cv2
from cv2 import aruco
import socket
import pickle
import struct
import urllib.request

url= 'http://192.168.43.147/cam-lo.jpg'
im=None

# Function to send data to ESP32
def send_data(client_socket, data):
    data = pickle.dumps(data)
    # Remove spaces from the serialized data
    data = data.replace(b' ', b'')
    message_size = struct.pack("L", len(data))  # Pack the message size as a long integer
    client_socket.sendall(message_size + data)

# ESP32 server address and port
esp32_ip = '192.168.43.232'  # Replace with your ESP32's IP address
esp32_port = 12345  # Replace with the port your ESP32 is listening on

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the ESP32 server
client_socket.connect((esp32_ip, esp32_port))



while True:
    img_resp=urllib.request.urlopen(url)
    imgnp=np.array(bytearray(img_resp.read()),dtype=np.uint8)
    frame = cv2.imdecode(imgnp,-1)
    # ret, frame = vid.read()

    # if not frame:
        # break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)
    parameters = cv2.aruco.DetectorParameters()
    detector = cv2.aruco.ArucoDetector(aruco_dict, parameters)
    markerCorners, markerIDs, rejectedImgPoints = detector.detectMarkers(frame)
    frame_markers = aruco.drawDetectedMarkers(frame.copy(), markerCorners, markerIDs)

    print(markerIDs)
    # coba = "hello123"
    # Example: sending marker IDs to ESP32
    send_data(client_socket, markerIDs)

    cv2.imshow("frame", frame_markers)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# vid.release()
cv2.destroyAllWindows()
client_socket.close()
