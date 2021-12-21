import cv2
import numpy as np

img = cv2.imread("lena.jpg", 1)             #read 0 greyscale ,1 colour, -1 as it is
img2=cv2.imread('messi5.jpg',1)
#print(img)                                 #view all cordinates

#img= np.zeros([512,512,3],np.uint8)                        #to create black window as img, numpy import

img= cv2.line(img,(0,0), (255,255), (255,0,0), 10)          #geometry shapes drawing
img= cv2.arrowedLine(img, (0,255),(300,455),(0,200,255),10)
img= cv2.rectangle(img, (255,255),(400,500),(0,255,0),10)   
img= cv2.circle(img, (255,100), 60, (140,50,20), -1)        #-1 fill
font= cv2.FONT_HERSHEY_SIMPLEX
img= cv2.putText(img, "Hafsa",(50,500),font,2,(255,255,255), 7,cv2.LINE_AA)

cv2.imshow('image', img)            #show in a window
cv2.imshow('image2', img2)
k= cv2.waitKey(0)

if k==27:                           #if press esc
    cv2.destroyAllWindows()
elif k== ord('s'):
    cv2.imwrite('lena_copy.jpg', img)   #make a copy 
    cv2.destroyAllWindows()

