# coding:utf-8
# import cv2
# cap = cv2.VideoCapture()
# flag = cap.isOpened()
# index = 1
# cap.open(0)
import cv2
import numpy as np
cap = cv2.VideoCapture(0)
cap.open(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
    dilated = cv2.dilate(thresh, kernel, iterations=3)
    
    contours= cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    print(np.shape(contours[0]))
    for contour in contours:
        contour = np.array(contour)
        x, y, w, h = cv2.boundingRect(contour)
        if w > 50 and h > 50:
            aspect_ratio = float(w) / h
            if 0.8 < aspect_ratio < 1.2:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
