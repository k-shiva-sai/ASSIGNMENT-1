#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np
import cv2
import matplotlib.pyplot as plt


# In[11]:


image=cv2.imread("C:\\Users\\Shiva\\Desktop\\LETS UPGRADE\\pichai.jpg")
image_nature=cv2.imread("C:\\Users\\Shiva\\Desktop\\LETS UPGRADE\\nature.jpg")
image_iron=cv2.imread("C:\\Users\\Shiva\\Desktop\\LETS UPGRADE\\iron.jpg")
cv2.imshow("CEO",image)
cv2.imshow("nature",image_nature)
cv2.imshow("iron",image_iron)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[13]:


cap=cv2.VideoCapture(0)
print("CLICK 1 FOR SUNDAR PICHAI BACKGROUND AND CLICK A TO EXIT FROM THE BACKGROUND")
print("CLICK 2 FOR BLUE BACKGROUND AND CLICK B TO EXIT FROM THE BACKGROUND")
print("CLICK 3 FOR GREEN BACKGOUND AND CLICK C TO EXIT FROM THE BACKGROUND")
print("CLICK 4 FOR RED BACKGROUND AND CLICK D TO EXIT FROM THE BACKGROUND")
print("CLICK 5 FOR NATURE BACKGROUND AND CLICK E TO EXIT FEOM THE BACKGROUND")
print("CLICK 6 FOR IRONMAN BACKGROUND BACKGROUND AND CLICK F TO EXIT FROM THE BACKGROUND")
print("CLICK X TO TURN OFF CAMERA")
while True:
    flag,frame=cap.read()
    if not flag:
        print("NOT POSSIBLE")
        break
    a1=cv2.waitKey(1)
    if a1==ord('1'):
        while(1):
            
            flag,frame2=cap.read(0)
            if not flag:
                print("not possible")
                break
            image=cv2.resize(image,(frame2.shape[1],frame2.shape[0]))
            blend=cv2.addWeighted(frame2,0.7,image,0.3,0.6)
            cv2.imshow("blend",blend)
            s1=cv2.waitKey(1)
            if s1==ord("a"):
                cv2.destroyWindow("blend")
                break
    elif a1==ord('2'):
        while(1):
            flag,frame3=cap.read(0)
            if not flag:
                print("not possible")
                break
            b,g,r=cv2.split(frame3)
            zeros=np.zeros(frame3.shape[:2],np.uint8)
            blue_back=cv2.merge([b,zeros,zeros])
            cv2.imshow("blue",blue_back)
            s2=cv2.waitKey(1)
            if s2==ord("b"):
                cv2.destroyWindow("blue")
                break
    elif a1==ord('3'):
        while(1):
            flag,frame4=cap.read(0)
            if not flag:
                print("not possible")
                break
            b,g,r=cv2.split(frame4)
            zeros=np.zeros(frame4.shape[:2],np.uint8)
            green_back=cv2.merge([zeros,g,zeros])
            cv2.imshow("green",green_back)
            s2=cv2.waitKey(1)
            if s2==ord("c"):
                cv2.destroyWindow("green")
                break
    elif a1==ord('4'):
        while(1):
            flag,frame4=cap.read(0)
            if not flag:
                print("not possible")
                break
            b,g,r=cv2.split(frame4)
            zeros=np.zeros(frame4.shape[:2],np.uint8)
            red_back=cv2.merge([zeros,zeros,r])
            cv2.imshow("red",red_back)
            s2=cv2.waitKey(1)
            if s2==ord("d"):
                cv2.destroyWindow("red")
                break
    elif a1==ord("5"):
        while True:
            flag,frame5=cap.read(0)
            if not flag:
                print("not possible")
                break
            image_nature=cv2.resize(image_nature,(frame5.shape[1],frame5.shape[0]))
            blend=cv2.addWeighted(frame5,0.7,image_nature,0.3,0.6)
            cv2.imshow("blend",blend)
            s1=cv2.waitKey(1)
            if s1==ord("e"):
                cv2.destroyWindow("blend")
                break
    elif a1==ord("6"):
        while True:
            flag,frame6=cap.read(0)
            if not flag:
                print("not possible")
                break
            image_iron=cv2.resize(image_iron,(frame6.shape[1],frame6.shape[0]))
            blend=cv2.addWeighted(frame6,0.7,image_iron,0.3,0.6)
            cv2.imshow("blend",blend)
            s1=cv2.waitKey(1)
            if s1==ord("f"):
                cv2.destroyWindow("blend")
                break
    cv2.imshow("webcam",frame)
    p=cv2.waitKey(1)
    if p==ord('x'):
        break
cap.release()
cv2.destroyAllWindows()


# In[ ]:




