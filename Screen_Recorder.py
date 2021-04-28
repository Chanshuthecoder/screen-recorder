# importing the required packages 
import pyautogui 
from PIL import ImageGrab
import cv2 
import numpy as np 
import keyboard

# Specify resolution 
resolution = pyautogui.size()

# Specify video codec 
codec = cv2.VideoWriter_fourcc(*'mp4v')


# Specify name of Output file 
filename = "Recording.mp4"

# Specify frames rate. We can choose any 
# value and experiment with it 
fps = 30.0


# Creating a VideoWriter object 
out = cv2.VideoWriter(filename, codec, fps, resolution) 

# check if a esc is pressed
print(keyboard.is_pressed('esc'))
while keyboard.is_pressed('esc')!=True: 
	# Take screenshot using PyAutoGUI 
	img = ImageGrab.grab(bbox=None)

	# Convert the screenshot to a numpy array 
	frame = np.array(img) 

	# Convert it from BGR(Blue, Green, Red) to 
	# RGB(Red, Green, Blue) 
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	currentMouseX, currentMouseY = pyautogui.position() 
	frame = cv2.circle(frame, (currentMouseX, currentMouseY), 15, (0,255,0), -1)
	# Write it to the output file 
	out.write(frame) 
	
	# Optional: Display the recording screen 
	# cv2.imshow('Live', frame) 
	
	# Stop recording when we press 'q' 
	# if cv2.waitKey(1) == ord('q'): 
	# 	break

# Release the Video writer 
out.release() 

# Destroy all windows 
# cv2.destroyAllWindows()



