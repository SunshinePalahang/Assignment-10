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
        name = "Scan Results is up!"
        pts2 = obj.rect
        cv2.putText(qr, name, (pts2 [0], pts2 [1]), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1,(0,0,0),2)
#for storing in text file
        f = open("Contact Tracing.txt", "w")
        f.write(f"{obj.data.decode('utf-8')}\n")
#for date and time
        date = datetime.datetime.now()
        f.write(date.strftime("Date: %m/%d/%y\n"))
        f.write(date.strftime("Time: %H:%M:%S"))
        f.close()

    cv2.imshow("Scanner", qr)
    cv2.waitKey(1)
    cv2.destroyAllWindows