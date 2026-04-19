import os 
import cv2 
#read__video
video_path = os.path.join('.','data','C:\\Users\\User\\Desktop\\Projects\\VID_20251227_110023.mp4')
video=cv2.VideoCapture(video_path)
#visualize_video
ret=True
while ret:
    ret, frame=video.read()
    cv2.imshow('video',frame)
    if cv2.waitKey(50) & 0xFF == ord('q'):
        break
video.release()
cv2.destroyAllWindows()