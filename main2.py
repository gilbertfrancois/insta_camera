import cv2
import numpy as np

if __name__ == "__main__":

    cap = cv2.VideoCapture()
    
    while True:
        ret, frame = cap.read()
        cv2.imshow(frame)
