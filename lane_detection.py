from tkinter import *
from tkvideo import tkvideo
import cv2
from moviepy.editor import *
import numpy as np

def show_vid():                                        
    player = tkvideo("D:\VIT\Sem 3\EDAI-3\lanedetection\input3.mp4", lmain, loop = 1, size = (600,400))
    player.play()

def show_vid2():
    player = tkvideo("D:\VIT\Sem 3\EDAI-3\lanedetection\output1.mp4", lmain2, loop = 1, size = (600,400))
    player.play()

def region_of_interest(image, vertices):
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, vertices, 255)
    regionoi = cv2.bitwise_and(image, mask)
    return regionoi

def process_image(image):
    #Convert the image color
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    #reduce noise from the image
    gauss_gray = cv2.GaussianBlur(gray_image, (5, 5), 0)
    
    #detect edges from the image
    canny = cv2.Canny(gauss_gray, 100, 120)

    #mask the unnecessary part
    vertices = [np.array(
                        [[0.15*image.shape[1],image.shape[0]],
                        [0.4*image.shape[1],0.65*image.shape[0]],
                        [0.72*image.shape[1],0.65*image.shape[0]],
                        [0.9*image.shape[1],image.shape[0]]],
                np.int32)]
    roi = region_of_interest(canny, vertices)

    return roi

clip1 = VideoFileClip("D:\VIT\Sem 3\EDAI-3\lanedetection\input3.mp4")
video_frame = clip1.fl_image(process_image)
video_frame.write_videofile('D:\VIT\Sem 3\EDAI-3\lanedetection\output1.mp4', audio=False)

if __name__ == '__main__':
    root = Tk()
    heading = Label(root, text="SY_Group")
    heading.pack()
    heading2 = Label(root,text="Lane-Line Detection",pady=20, font=('arial',45,'bold'))                                 
    heading2.pack()
    
    lmain = Label(master=root)
    lmain2 = Label(master=root)
    lmain.pack(side = LEFT)
    lmain2.pack(side = RIGHT)
    
    root.title("Lane-line detection")            
    root.geometry("1250x720+130+40") 
    
    exitbutton = Button(root, text='Quit',fg="red",command=root.destroy).pack(side = BOTTOM)
    show_vid()
    show_vid2()
    root.mainloop()