import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)

while True:
  _ , frame = cap.read()

  hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

  #Use the color picker to get the values......we can define any color not just red
  red_lower = np.array([150, 150, 50])     
  red_upper = np.array([180, 255, 150])

  mask = cv2.inRange(hsv, red_lower, red_upper)

  kernal = np.ones((5,5))
  dilate = cv2.dilate(mask, kernal)
  res = cv2.bitwise_and(frame, frame, mask = mask)

  contours, hierarchy = cv2.findContours(dilate, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

  cv2.drawContours(frame, contours, -1, (255,0,0), 4)
  for c in contours:
    area = cv2.contourArea(c)
    x,y,w,h = cv2.boundingRect(c)
    img = cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 2)
#    cv2.putText(img, "Cap is placed", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255))
    print len(contours)
      
  cv2.imshow("Color Tracking", frame) 
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()
