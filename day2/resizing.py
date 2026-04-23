import os
import cv2
img = cv2.imread(os.path.join('.','data','C:\\Users\\User\\Desktop\\Projects\\day1\\data\\IMG_20251211_194645.jpg'))
#resize
resized_img = cv2.resize(img, (300, 300))
#visualize
cv2.imshow('resized image', resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()