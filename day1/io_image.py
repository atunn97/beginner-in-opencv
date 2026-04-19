import os 
import cv2
#read_image
image_path = os.path.join('.','data','C:\\Users\\User\\Desktop\\Projects\\IMG_20251211_194645.jpg')
img= cv2.imread(image_path)
#write_image
cv2.imwrite(os.path.join('.','data','anhdiemdanh.jpg'),img)
#visualize_image
cv2.imshow('anhdiemdanh',img)
cv2.waitKey(0)