import cv2
import numpy as np

cap = cv2.VideoCapture('test.mp4')
while True :
    isTrue, frame=cap.read()
    cv2.imshow("Original Image", frame)
    laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    laplacian = np.uint8(laplacian)
    cv2.imshow('Laplacian', laplacian)
    edges = cv2.Canny(frame,80,80)
    cv2.imshow('Canny', edges)
    if cv2.waitKey(20) & 0xFF==ord('d'):
        break



cap.release()
cv2.destroyAllWindows()




