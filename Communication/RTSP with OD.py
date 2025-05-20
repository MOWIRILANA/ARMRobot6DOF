import cv2

# URL for the ESP32-CAM's RTSP stream
rtsp_stream_url = 'rtsp://192.168.137.191:8554/mjpeg/1'  # Replace with your ESP32-CAM's RTSP stream URL

# Capture video from the RTSP stream
cap = cv2.VideoCapture(rtsp_stream_url)

# Check if the video capture is successful
if not cap.isOpened():
    print("Error opening video stream or file")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Display the frame
    cv2.imshow('ESP32-CAM Stream', frame)

    # Close the window and break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
