import os
import cv2
img = cv2.imread(os.path.join('.', 'data', 'C:\\Users\\User\\Desktop\\Projects\\day1\\data\\IMG_20251211_194645.jpg'))
# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Apply global thresholding
global_thresh_value = 127  # Threshold value (0-255)
_, global_thresh = cv2.threshold(gray, global_thresh_value, 255, cv2.THRESH_BINARY)
# Apply adaptive thresholding
adaptive_thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
# Visualize the results
cv2.imshow('Original Image', img)
cv2.imshow('Global Thresholding', global_thresh)
cv2.imshow('Adaptive Thresholding', adaptive_thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()