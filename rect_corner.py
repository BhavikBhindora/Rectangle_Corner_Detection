#Import Library
import numpy as np
import cv2
import matplotlib.pyplot as plt
import imutils
from scipy import spatial
import matplotlib as mpl
import numpy as np
import pandas as pd

#Read Image
path = r"Path/To/Your/Mask/Image"
img = cv2.imread(path)
# mask = np.zeros(img.shape, dtype=np.uint8)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Find Contours
contours = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

c = max(contours[0], key = cv2.contourArea)
x,y,w,h = cv2.boundingRect(c)
polygon = img.copy()
a= c.max()
b = c.min()

#Draw Rectangle and Circle
img= cv2.rectangle(polygon, (x, y), (x + w, y + h), (0,255,0), 5)
cv2.circle(polygon,(x+w,y+h),10,(0,0,255),-1)
cv2.circle(polygon,(x,y),10,(255,0,0),-1) 
cv2.circle(polygon,(x+w,y),10,(0,255,0),-1) 
cv2.circle(polygon,(x,y+h),10,(255,0,255),-1) 
print(x,y,w,h)
print(a,b)


#Plot the Fig.
mpl.rcParams['figure.figsize'] = (12,12); 
plt.figure()
plt.subplot(121);plt.imshow(gray);plt.axis('off');plt.title('gray')
# plt.subplot(132);plt.imshow(morph);plt.axis('off');plt.title('dilate')
plt.subplot(122);plt.imshow(polygon);plt.axis('off');plt.title('Image') 
