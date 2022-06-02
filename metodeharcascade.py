
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
