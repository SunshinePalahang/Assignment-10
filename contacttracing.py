import cv2
import numpy as np
from pyzbar.pyzbar import decode
import datetime

#start the cam
cam = cv2.VideoCapture(0)
cam.set (3, 1080)
cam.set (4, 720)

i = True
while i == True:
    _, qr = cam.read()
    for obj in decode(qr):
#for effects
        pts = np.array([obj.polygon],np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(qr, [pts], True, (120, 0, 120), 5)
#for storing in text file
        f = open("Contact Tracing.txt", "w")
        f.write(f"{obj.data.decode('utf-8')}\n")
    cv2.imshow("Scanner", qr)
    cv2.waitKey(1)