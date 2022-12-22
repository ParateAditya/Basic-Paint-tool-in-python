
import cv2 as cv
import numpy as np

def nothing(x):
    pass



img = np.zeros((600,1000,3), np.uint8)
img[:] = (255,255,255)                      #---> creates a blank paint_tool

drawBool = False
x1=0
y1=0
def draw(event , x , y , flags , params  ):
    global drawBool , x1 , y1
    if event == cv.EVENT_LBUTTONDOWN:
        if s>0 and d==1 and R==1 :
            cv.setTrackbarPos('Rectangle' , 'Trackbar' , 0)
            cv.setTrackbarPos('Circle' , 'Trackbar' , 0)

        elif eraser > 0 :
            drawBool = True
            x1 = x
            y1 = y
        
        elif s>0 and d==1:
            cv.circle(img ,(x,y) , s , (b,g,r) , t)
        elif R==1 and d==1 :
            drawBool = True
            x1 = x
            y1 = y
        elif d==0 :
            drawBool = True
            x1 = x
            y1 = y
            cv.setTrackbarPos('Rectangle' , 'Trackbar' , 0)
            cv.setTrackbarPos('Circle' , 'Trackbar' , 0)
        
    elif event == cv.EVENT_MOUSEMOVE :
        if drawBool:
            if eraser > 0:
                cv.line(img  , (x,y),(x1,y1) , (255,255,255),eraser)
                x1 ,y1 = x,y
            elif d==0:
                cv.line(img  , (x,y),(x1,y1) , (b,g,r),t)
                x1 ,y1 = x,y
            elif d==1 and R==1:
                cv.rectangle(img ,  (x,y) , (x1,y1) , (b,g,r) , -1)
            

    elif event == cv.EVENT_LBUTTONUP:
        drawBool = False

        
cv.imshow('paint_tool' , img)
trackbar = np.zeros((100,500,3), np.uint8)
trackbar[:] = (0,0,0)
cv.imshow('Trackbar' , trackbar)


cv.createTrackbar('Red' , 'Trackbar' , 0 , 250  ,nothing )
cv.createTrackbar('Green' , 'Trackbar' , 0 , 250  ,nothing )
cv.createTrackbar('Blue' , 'Trackbar' , 0 , 250  , nothing )
cv.createTrackbar('Thickness' , 'Trackbar' , 1 , 50 , nothing)       #--->thickness of pencil
cv.createTrackbar('DrawShape' , 'Trackbar' , 0,1,nothing)            #--->switch between pencil and Shape
cv.createTrackbar('Circle' ,  'Trackbar' , 0,100 , nothing)          #--->Draw circle of radius 1-100
cv.createTrackbar('Rectangle' , 'Trackbar' , 0,1,nothing)            #--->Draw Rectangle if 1 
cv.createTrackbar('EraserSize' , 'Trackbar' , 0,100 , nothing)       


while True :
    cv.setMouseCallback('paint_tool' , draw)
    cv.imshow('paint_tool' , img)
    cv.imshow('Trackbar' , trackbar)
    k = cv.waitKey(1) & 0xFF 
    if k==27:
        break
    r = cv.getTrackbarPos('Red' , 'Trackbar')
    g = cv.getTrackbarPos('Green' , 'Trackbar')
    b = cv.getTrackbarPos('Blue' , 'Trackbar')
    t = cv.getTrackbarPos('Thickness' , 'Trackbar')
    d = cv.getTrackbarPos('DrawShape' , 'Trackbar')
    s = cv.getTrackbarPos('Circle' , 'Trackbar')
    R = cv.getTrackbarPos('Rectangle' , 'Trackbar')
    eraser = cv.getTrackbarPos('EraserSize' , 'Trackbar')
    trackbar[:] = (b,g,r)

cv.destroyAllWindows()