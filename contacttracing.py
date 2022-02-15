import cv2
import numpy as np
from pyzbar.pyzbar import decode
import datetime

#start the cam
cam = cv2.VideoCapture(0)
cam.set (3, 1080)
cam.set (4, 720)

