import cv2
import numpy as np

cap = cv2.VideoCapture("Red Dot.mp4") #Capture Video nya

ret, frame1 = cap.read() #Untuk membaca frame1 dan frame2 dari video
ret, frame2 = cap.read()

while cap.isOpened():
    diff = cv2.absdiff(frame1, frame2) # Untuk menemukan perubahan dalam video
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY) # Dari perubahan tersebut, kita gunakan pengubah warna dan blur
    blur = cv2.GaussianBlur(gray, (5,5), 0) # Hal ini dilakukan untuk mempermudah melihat perubahannya
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=6)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #hasil countour

    for contour in contours: # Untuk menghasilkan efek kotak disekitar perubahan gerak kotak
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255,0), 2)

    cv2.imshow("Lingkaran apa tu man?", frame1)
    frame1 = frame2
    ret, frame2 = cap.read()

    key = cv2.waitKey(1)
    if key == 27: # Pencet esc untuk mematikan program
        break

cap.release()
cv2.destroyAllWindows()