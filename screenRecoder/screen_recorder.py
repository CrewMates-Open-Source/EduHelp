#Import Required Modules
from PIL import ImageGrab
import numpy as np
import cv2
import datetime
from win32api import GetSystemMetrics

#Get the dimensions of the screen and customize the part of screen you want to record.
#Here,Recording the whole screen.
width=GetSystemMetrics(0)
height=GetSystemMetrics(1)

# retrieving the time stamp and saving the recorded files.
time_stamp= datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
file_name=f'{time_stamp}.mp4'

video=cv2.VideoWriter_fourcc('m','p','4','v')
screen_recorder=cv2.VideoWriter(file_name,video,3.0,(width,height))
while True:
    img=ImageGrab.grab(bbox=(0,0,width,height)) #takes snapshot of the screen
    np_img=np.array(img)
    final_img=cv2.cvtColor(np_img,cv2.COLOR_BGR2RGB) #stored image is in BGR format,so need to convert it to RGB.

    #Here,adding an extra feature to screen recorder to allow webcam to capture image and taking the snapshot of that too with the screen.
    webcam=cv2.VideoCapture(0) #Here,argument is 0 ,because using PC default camera
    _, frame= webcam.read()
    frame_height, frame_width, _ = frame.shape
    final_img[0:frame_height,0:frame_width, :]=frame[0:frame_height, 0:frame_width, :] #overlay the webcam frame over the screen.
    cv2.imshow('record_screen',final_img)
    screen_recorder.write(final_img)

    if cv2.waitKey(10)==ord('t'):#snapshot will be capctured ,until 't' is pressed.
        break
cv2.destroyAllWindows()

