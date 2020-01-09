# ___________________Improve adaptive Gaussian Mixture model for background subtraction___________________________--

import numpy as np
import cv2

cap = cv2.VideoCapture('/home/paython/Videos/4K Video Downloader/Pogba Penalty, 10 seconds walking.mp4')

foreground_background = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    foreground_mask = foreground_background.apply(frame)
    cv2.imshow('output',foreground_mask)
    if cv2.waitKey(1)==13:
        break
cap.release()
cv2.destroyAllWindows()
