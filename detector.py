import math

import cv2
import numpy as np

HSV_LOWER = np.array([100, 120, 70])
HSV_UPPER = np.array([130, 255, 255])
MIN_AREA = 150
MIN_CIRCULARITY = 0.85
KERNEL = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))


def detect(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, HSV_LOWER, HSV_UPPER)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, KERNEL)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, KERNEL)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    circles = [c for c in contours if is_circle(c)]
    if not circles:
        return None

    (x, y), _ = cv2.minEnclosingCircle(max(circles, key=cv2.contourArea))
    return x, y


def is_circle(contour):
    area = cv2.contourArea(contour)
    if area < MIN_AREA:
        return False
    perimeter = cv2.arcLength(contour, True)
    return 4 * math.pi * area / perimeter**2 >= MIN_CIRCULARITY
