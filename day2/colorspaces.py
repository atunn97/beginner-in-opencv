import os
import cv2
img= cv2.imread(os.path.join('.','data','C:\\Users\\User\\Desktop\\Projects\\day1\\data\\IMG_20251211_194645.jpg'))
#convert to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#visualize
cv2.imshow('grayscale image', gray_img)
cv2.imshow('rgb image', img_rgb)
cv2.waitKey(0)
""" Tóm tắt logic sử dụng
Nhận diện màu → cvtColor(BGR→HSV) → inRange() → bitwise_and()
Xử lý nhanh → cvtColor(BGR→Gray)
Tăng chất lượng ảnh → equalizeHist() / LAB
Phân tích sâu → split() từng kênh """
