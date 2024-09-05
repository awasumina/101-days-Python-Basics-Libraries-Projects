# pip install opencv-python

import cv2

img_capture = cv2.VideoCapture(0) # id of the webcam as in laptop we have only 1 inbuilt webcam so it is assigned 1 , if you have multiple webcams assign it in similar way

result = True

while result :
    ret, frame = img_capture.read()
    cv2.imwrite('test1.jpg', frame)
    result = False
    print("Image Captured")

img_capture.release()
   
