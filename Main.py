from google.colab.patches import cv2_imshow
import cv2
import numpy as np

def classify(img):
  img = cv2.imread(img)
  gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
  ret, thresh = cv2.threshold(gray, 127, 255, 1)
  contours, h = cv2.findContours(thresh, 1, 2)
  for cnt in contours:
      approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
      print(len(approx))
      if len(approx) == 5:
          return"pentagon"
          cv2.drawContours(img, [cnt], 0, 255, -1)
      elif len(approx) == 3:
          return "triangle"
          cv2.drawContours(img, [cnt], 0, (0, 255, 0), -1)
      elif len(approx) == 4:
          return "square"
          cv2.drawContours(img, [cnt], 0, (0, 0, 255), -1)
      elif len(approx) == 9:
          return "half-circle"
          cv2.drawContours(img, [cnt], 0, (255, 255, 0), -1)
      elif len(approx) > 15:
          return "circle"
          cv2.drawContours(img, [cnt], 0, (0, 255, 255), -1)
