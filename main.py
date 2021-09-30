import cv2
img = cv2.imread("test.jpg.jpg")

grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eyes_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")

faces = face_cascade.detectMultiScale(grey, 1.1, 5)
eyes = eyes_cascade.detectMultiScale(grey, 1.1, 5)
for x, y, w, h in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 3)

for x, y, w, h in eyes:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)



cv2.imshow("Face", img)
cv2.waitKey(0)