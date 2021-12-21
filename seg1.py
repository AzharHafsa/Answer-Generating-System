import cv2
import numpy as np

image = cv2.imread('1.jpg')
cv2.imshow('Orginal',image)                

gray= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)        
cv2.imshow('Grayscaled',gray)


ret, thresh = cv2.threshold(gray,50,255,cv2.THRESH_BINARY_INV)  
cv2.imshow('Thresholded', thresh)


kernal = np.ones((10,20), np.uint8)
img_dilation = cv2.dilate(thresh, kernal, iterations=1)     
cv2.imshow('Dilated', img_dilation) 


ctrs, hier = cv2.findContours(img_dilation.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 
 

sorted_ctrs = sorted(ctrs, key= lambda ctr: cv2.boundingRect(ctr)[0])       

for i, ctr in enumerate(sorted_ctrs):
    x,y,w,h = cv2.boundingRect(ctr)

    roi = image[y: y+h, x:x+w]      

    cv2.imshow('segment no: '+ str(i), roi)         
    cv2.rectangle(image, (x,y), (x+w, y+h), (90,0,255), 2)  
    

cv2.imshow('marked area', image)    
cv2.waitKey(0)

if k==27:                           
    cv2.destroyAllWindows()
    