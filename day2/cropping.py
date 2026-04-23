import os
import cv2
img= cv2.imread(os.path.join('.','data','C:\\Users\\User\\Desktop\\Projects\\day1\\data\\IMG_20251211_194645.jpg'))
#crop
cropped_img = img[100:400, 100:400]
#visualize
cv2.imshow('cropped image', cropped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()