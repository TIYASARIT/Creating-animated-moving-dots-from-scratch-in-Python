#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 15:47:58 2023

@author: ts4781 (Tiyasa Sarkr)

"""

import cv2
import time
import os
import numpy as np
import glob
from PIL import Image

# cam = cv2.VideoCapture("/home/ts4781/Downloads/alb_ufo003_1080p.mp4")
  
# try:
      
#     # creating a folder named data
#     if not os.path.exists('data'):
#         os.makedirs('data')
  
# # if not created then raise error
# except OSError:
#     print ('Error: Creating directory of data')
  
# # frame
# currentframe = 0
# time_start = time.time()
# # Find the number of frames
# video_length = int(cam.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
# print("Number of frames: ", video_length)
# while(True):
      
#     # reading from frame
#     ret,frame = cam.read()
  
#     if ret:
#         # if video is still left continue creating images
#         name = './data/frame' + str(currentframe) + '.jpg'
#         print ('Creating...' + name)
  
#         # writing the extracted images
#         cv2.imwrite(name, frame)
  
#         # increasing counter so that it will
#         # show how many frames are created
#         currentframe += 1
#     else:
#         time_end = time.time()
#         break
  
# # Release all space and windows once done
# cam.release()
# print("Stats")
# print ("Done extracting frames.\n%d frames extracted" % currentframe)
# print ("It took %d seconds forconversion." % (time_end-time_start))
# cv2.destroyAllWindows()

## Background subtraction

frame_loc = 'home/data/* .jpg'
image_list = []


for filename in glob.glob(frame_loc):
    print('t')
    print(filename)
    im = Image.open(filename)
    image_list.append((im))

cv2.imread('home/ts4781/data/frame0.jpg')