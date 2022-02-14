import cv2
import webbrowser

#start the cam
cam = cv2.VideoCapture(0)
#detect qrcode
detect = cv2.QRCodeDetector

while True:
    _, img = cap.read()