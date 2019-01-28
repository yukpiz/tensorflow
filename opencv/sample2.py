import numpy as np
import cv2 as cv

print(cv.__path__)


def f(fpath):
    face_cascade = cv.CascadeClassifier('/home/yukpiz/.pyenv/versions/3.6.5/lib/python3.6/site-packages/cv2/data/haarcascade_frontalface_default.xml')
    eye_cascade = cv.CascadeClassifier('/home/yukpiz/.pyenv/versions/3.6.5/lib/python3.6/site-packages/cv2/data/haarcascade_eye.xml')
    img = cv.imread(fpath)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    return img

img = f('data/src/photo1.jpg')
cv.imwrite('data/dst/result1.jpg', img)

img = f('data/src/photo2.png')
cv.imwrite('data/dst/result2.png', img)

img = f('data/src/photo3.jpg')
cv.imwrite('data/dst/result3.jpg', img)

img = f('data/src/photo4.png')
cv.imwrite('data/dst/result4.png', img)

