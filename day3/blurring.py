import os
import cv2
img = cv2.imread(os.path.join('.', 'data', 'C:\\Users\\User\\Desktop\\Projects\\day1\\data\\IMG_20251211_194645.jpg'))
k_size = 15  # Kernel size for blurring (must be odd)
# Apply Gaussian blur
""" Công dụng

Làm mờ bằng bộ lọc Gaussian (trung bình có trọng số, pixel gần tâm được ưu tiên hơn).
gaussian_blur = cv2.GaussianBlur(img, (k_size, k_size), 0) """
# Apply median blur
""" Cực mạnh với:

Salt-and-pepper noise
(nhiễu chấm trắng đen)
median_blur = cv2.medianBlur(img, k_size) """
# Apply bilateral filter
""" Công dụng

Làm mờ nhưng giữ biên (edge-preserving smoothing).
bilateral_blur = cv2.bilateralFilter(img, k_size, 75, 75) """
# Visualize the results
cv2.imshow('Original Image', img)
cv2.imshow('Gaussian Blur', gaussian_blur)
cv2.imshow('Median Blur', median_blur)
cv2.imshow('Bilateral Blur', bilateral_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()