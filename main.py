import cv2
#openCV module


face_cascade = cv2.CascadeClassifier('for_face.xml')
cap = cv2.VideoCapture('v.mp4')
# use 0 (inbuilt webcam) -1 (for external webcam) instead of v.mp4 to get results from webcam


while True:
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray, 1.9, 6)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 1)


    cv2.imshow('img', img)
    k = cv2.waitKey(2) & 0xff
    if k==27:
        break
        
cap.release()
