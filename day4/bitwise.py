import cv2 as cv
import numpy as np
# Load the image
blank = np.zeros((400, 400), dtype='uint8')
# Draw two rectangles on the blank image
rectangle1 = cv.rectangle(blank.copy(), (50, 50), (350, 350), 255, -1)  # White rectangle
circle1 = cv.circle(blank.copy(), (200, 200), 200, 255, -1)  # White circle
# Perform bitwise AND operation
bitwise_and = cv.bitwise_and(rectangle1, circle1)
# Perform bitwise OR operation
bitwise_or = cv.bitwise_or(rectangle1, circle1)
# Perform bitwise XOR operation
bitwise_xor = cv.bitwise_xor(rectangle1, circle1)
# Visualize the results
cv.imshow('Rectangle', rectangle1)
cv.imshow('Circle', circle1)
cv.imshow('Bitwise AND', bitwise_and)
cv.imshow('Bitwise OR', bitwise_or)
cv.imshow('Bitwise XOR', bitwise_xor)
cv.waitKey(0)
cv.destroyAllWindows()
