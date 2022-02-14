import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

#start the cam
cam = cv2.VideoCapture(0)
#detect qrcode
detect = cv2.QRCodeDetector

while True:
    _, img = cam.read()

    detect = pyzbar.decode(img)
    for obj in detect:
        print(obj.data)

    cv2.imshow("Frame", img)
    key = cv2.waitKey(1)
    if key == 1:
        break
