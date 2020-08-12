import cv2
import numpy as np
import os
cap = cv2.VideoCapture(0)

try:
    os.listdir("Camera_image")
except:
    os.mkdir("Camera_image")

try:
    os.listdir("Camera_video")
except:
    os.mkdir("Camera_video")

while True:
    flag, img = cap.read()
    cv2.imshow("Camera", img)

    if cv2.waitKey(1) & 0xFF == ord(' '):
        fold = os.walk("Camera_image")
        for i in fold:
            file = i[2]
        path = "Camera_image\\"
        if file == []:
            image_name = "image 1.jpg"
            image_path = path + image_name
            cv2.imwrite(image_path, img)
            cv2.imshow(image_name, img)
        else:
            number = int(file[-1][6:7]) + 1
            image_name = "image " + str(number) + ".jpg"
            image_path = path + image_name
            cv2.imwrite(image_path, img)
            cv2.imshow(image_name, img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()