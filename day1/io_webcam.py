import cv2
#read_webcam
webcam = cv2.VideoCapture(0)
#visualize_webcam

while True:
    ret, frame = webcam.read()

    if not ret:
        break

    cv2.imshow('frame', frame)

    if cv2.waitKey(500) & 0xFF == ord('q'):
        break
webcam.release()
cv2.destroyAllWindows()