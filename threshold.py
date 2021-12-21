import cv2 
import numpy as np
from matplotlib import colors, pyplot as plt

img= cv2.imread('sample1.jpeg', 0)

_, th1= cv2.threshold(img,90,255,cv2.THRESH_BINARY)
#_, th2= cv2.threshold(img,90,255,cv2.THRESH_BINARY_INV)
th3 = cv2.adaptiveThreshold(img,255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,3,12)

kernal=np.ones((2,2), np.uint8)                 #dilations 1,1 means no changes.

dilation= cv2.dilate(th1,kernal,iterations=1)       #marks remove spread
erosion= cv2.erode(th1, kernal,iterations=1)        #borders shrink - suitable
closing= cv2.morphologyEx(th1, cv2.MORPH_CLOSE, kernal) #dilation and then erosion 

# cv2.imshow('erosion',erosion)       #suitable
# cv2.imshow('dilation',dilation)
# cv2.imshow('closing',closing)
# cv2.waitKey(0)

titles = ['img','th1','th3','dilation','erosion','closing']     #in one window
images= [img, th1, th3, dilation,erosion, closing]

for i in range(6):
    plt.subplot(2,3,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()