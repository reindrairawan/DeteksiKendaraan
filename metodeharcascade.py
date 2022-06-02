import cv2
from time import sleep

pathcascade = 'cars.xml'
pathvideo = 'video.mp4'

cap  = cv2.VideoCapture(pathvideo)
cascade = cv2.CascadeClassifier(pathcascade)
crop_dir = 'crop/'
iterasi = 10
i=0

delay = 200
detect = []
offset = 6 #allowable arror between pixel
car=0
z=0
counter_line_positon = 550


def center_handle(x,y,w,h):
    x1=int(w/2)
    y1=int(h/2)
    cx= x+x1
    cy= y+y1
    return cx,cy



while True:
    ret, framecars = cap.read()
    car_img = framecars.copy()
    time = float(1/delay)
    sleep(time)

    
    if(type(framecars)== type(None)):
        break

  
    # z = z+1
       
    gray = cv2.cvtColor(framecars, cv2.COLOR_BGR2GRAY)

    cars = cascade.detectMultiScale(gray, 1.1, 1)
    cv2.line(framecars, (25, counter_line_positon), (1200, counter_line_positon), (255,127,0),3)
   

    
    for (x,y,w,h) in cars:
        cv2.rectangle(framecars,(x,y),(x+w,y+h), (0,255,0),2)
        center = center_handle(x,y,w,h)
        car_img = framecars[y:y+h,x:x+w]
        z=z+1
        
        detect.append(center)
        # cv2.circle(framecars, center, 4, (0,0,255), -1)

        for (x,y) in detect:
            if y<(counter_line_positon+offset) and y>(counter_line_positon-offset):
                car+=1


        
        cv2.line(framecars,(25,counter_line_positon),(1200,counter_line_positon),(0,127,255),3)
        # cv2.imwrite(crop_dir+ str(i) +'--' +str(z)+'.jpg',car_img)
        
        detect.remove((x,y))
        print("Hitung Kendaraan:"+str(car))


        cv2.putText(framecars, "Hitung:" +str(car), (450,70), cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255),5)

        cv2.imshow('video', framecars)

   
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 

cv2.destroyAllWindows()
cap.release()