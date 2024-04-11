# generate video frames

import cv2
import time
import os
import numpy as np
import glob
from PIL import Image
# def video_to_frames(input_loc, output_loc):
#     """Function to extract frames from input video file
#     and save them as separate frames in an output directory.
#     Args:
#         input_loc: Input video file.
#         output_loc: Output directory to save the frames.
#     Returns:
#         None
#     """
#     try:
#         os.mkdir(output_loc)
#     except OSError:
#         pass
#     # Log the time
#     time_start = time.time()
#     # Start capturing the feed
#     cap = cv2.VideoCapture(input_loc)
#     # Find the number of frames
#     video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
#     print ("Number of frames: ", video_length)
#     count = 0
#     print ("Converting video..\n")
#     # Start converting the video
#     while cap.isOpened():
#         # Extract the frame
#         ret, frame = cap.read()
#         if not ret:
#             continue
#         # Write the results back to output location.
#         cv2.imwrite(output_loc + "/%#05d.jpg" % (count+1), frame)
#         count = count + 1
#         # If there are no more frames left
#         if (count > (video_length-1)):
#             # Log the time again
#             time_end = time.time()
#             # Release the feed
#             cap.release()
#             # Print stats
#             print ("Done extracting frames.\n%d frames extracted" % count)
#             print ("It took %d seconds forconversion." % (time_end-time_start))
#             break


# if __name__=="__main__":

#     input_loc = '/home/ts4781/Downloads/alb_ufo003_1080p.mp4'
#     output_loc = 'home/ts4781/video_create/Frames_ufo'
#     video_to_frames(input_loc, output_loc)
#     # frame_1 = cv2.imread('C:/Users/TIYASA/OneDrive/Documents/animation/frames_ufo/00038.jpg')
#     # find_ROI(frame_1)

# Read the video from specified path
cam = cv2.VideoCapture("/home/ts4781/Downloads/alb_ufo003_1080p.mp4")
  
try:
      
    # creating a folder named data
    if not os.path.exists('data'):
        os.makedirs('data')
  
# if not created then raise error
except OSError:
    print ('Error: Creating directory of data')
  
# frame
currentframe = 0
time_start = time.time()
# Find the number of frames
video_length = int(cam.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
print("Number of frames: ", video_length)
while(True):
      
    # reading from frame
    ret,frame = cam.read()
  
    if ret:
        # if video is still left continue creating images
        name = './data/frame' + str(currentframe) + '.jpg'
        print ('Creating...' + name)
  
        # writing the extracted images
        cv2.imwrite(name, frame)
  
        # increasing counter so that it will
        # show how many frames are created
        currentframe += 1
    else:
        time_end = time.time()
        break
  
# Release all space and windows once done
cam.release()
print("Stats")
print ("Done extracting frames.\n%d frames extracted" % currentframe)
print ("It took %d seconds forconversion." % (time_end-time_start))
cv2.destroyAllWindows()

## Background subtraction

frame_loc = 'home/ts4781/data/*.jpg'
image_list = []
for filename in glob.glob(frame_loc):
    im = Image.open(filename)
    image_list.append(np.asarray(im))