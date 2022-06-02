from statistics import median_high
import cv2
import numpy as np
import sys

#untuk get videonya
cap = cv2.VideoCapture('Video.mp4')

min_width_react =80   #min with reactangle

min_height_react =80   #min height reactangle

counter_line_positon = 550

#inisialisasi substructor
algo = cv2.bgsegm.createBackgroundSubtractorMOG()

# algo = cv2.createBackgroundSubtractorMOG2()

def center_handle(x,y,w,h):
    x1=int(w/2)
    y1=int(h/2)
    cx= x+x1
    cy= y+y1
    return cx,cy

detect = []
offset = 6 #allowable arror between pixel
counter=0

while True:
    ret,frame1 = cap.read()
    gray = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(3,3),5)
    
    # set ke frame
    img_sub = algo.apply(blur)
    dilat = cv2.dilate(img_sub,np.ones((5,5)))
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
    dilatade = cv2.morphologyEx(dilat, cv2.MORPH_CLOSE, kernel)
    dilatade = cv2.morphologyEx(dilatade, cv2.MORPH_CLOSE, kernel)
    countershape,h = cv2.findContours(dilatade, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # cv2.imshow('Deteksi', dilatade)

    cv2.line(frame1,(25,counter_line_positon),(1200,counter_line_positon),(255,127,0),3)


    for (i,c) in enumerate(countershape):
        (x,y,w,h) = cv2.boundingRect(c)
        validation_counter = (w>= min_width_react) and (h>=min_height_react)
        if not validation_counter:
            continue

        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(frame1,"Hitung:"+str(counter),(x,y-20),cv2.FONT_HERSHEY_COMPLEX, 1, (255,244,0),2)



        center = center_handle(x,y,w,h)
        detect.append(center)
        cv2.circle(frame1, center,4, (0,0,255),-1)

        for (x,y) in detect:
            if y<(counter_line_positon+offset) and y>(counter_line_positon-offset):
                counter+=1
        cv2.line(frame1,(25,counter_line_positon),(1200,counter_line_positon),(0,127,255),3)
        detect.remove((x,y))
        print("Hitung Kendaraan:"+str(counter))


    cv2.putText(frame1,"Hitung:"+str(counter),(450,70),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255),5)
    
        
    cv2.imshow('Video Original', frame1)

    if cv2.waitKey(1) == 13:
        break

cv2.destroyAllWindows()
cap.release()
