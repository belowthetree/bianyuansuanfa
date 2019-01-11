import os
import matplotlib.pyplot as plt
import cv2
import numpy as np

def get_EuclideanDistance(x,y):
myx = np.array(x)
myy = np.array(y)
return np.sqrt(np.sum((myx-myy)*(myx-myy)))

dir = os.listdir('./train')

if name == 'main':

print('loading %s ...'%dir[1])
print('working')
image1 = cv2.imread('./train/'+dir[1])
w = image1.shape[1]
h = image1.shape[0]
image2 = np.zeros((h,w,3), np.uint8)

black = np.array([0,0,0])
white = np.array([255,255,255])
centercolor = np.array([125,125,125])
plt.ion()
i = 0
for y in range(0,h-1):
    for x in range(0,w-1):

        down = image1[y+1,x,:]
        right = image1[y,x+1,:]

        here = image1[y,x,:]
        here2 = here
        right2 = right
        down2 = down
        if get_EuclideanDistance(here2,down2) > 16 and get_EuclideanDistance(here2,right2) > 16 :
            image2[y,x,:]=black
        elif get_EuclideanDistance(here2,down2) <=16 and get_EuclideanDistance(here2,right2)<=16:
            image2[y,x,:] = white
        else:
            image2[y,x,:] = centercolor

        i += 1
        if i %2000 == 0:
            plt.imshow(image2)
            plt.pause(0.1)
 
print("完成")
plt.show()
