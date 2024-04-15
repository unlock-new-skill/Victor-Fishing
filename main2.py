import numpy as np
from PIL import ImageGrab
import time
import os
from datetime import datetime
import cv2
import pyautogui

x1, y1, x2, y2 = 658, 686, 1152, 737

save_folder = "images"

if not os.path.exists(save_folder):
    os.makedirs(save_folder)


def detect_color():
    # COLOR FOR DETECT ALL ISLAND 
    target_colors = [
        (219, 42, 22),
        (221, 45, 19),
        (221, 46, 23),
        (222, 38, 15),
        (222, 38, 15),
        (215, 42, 12),
        (216, 44, 23)
    ]
    
   
    screenshot = np.array(ImageGrab.grab(bbox=(x1, y1, x2, y2)))
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d-%H%M%S-%f")[:-3]
    image_path = os.path.join(save_folder, f"{timestamp}.png")
   
    bgr_image = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
    
    for target_color in target_colors:
        target_bgr = target_color[:3][::-1]  # Chuyển từ RGB sang BGR
        
        lower_color = np.array(target_bgr, dtype="uint8")
        upper_color = np.array(target_bgr, dtype="uint8")

        mask = cv2.inRange(bgr_image, lower_color, upper_color)

        count = cv2.countNonZero(mask)

        if count > 0:
           
            with open("./log.txt", "a") as log_file:
                log_file.write("Detected\n")
            print("Detected")
            return True
    
    return False

  

def perform_action():
   
    pyautogui.click(x=1200, y=689)
    time.sleep(1)
    pyautogui.click(x=950, y=689)
    time.sleep(7)
    

counter = 0

while True:
    ok = detect_color()
    print(ok)
        
    if ok:
        perform_action()
        counter = 0
    else:
        print(counter)
        if(counter > 100):
            
            pyautogui.click(x=950, y=689)
            counter = 0
        else:
            counter += 1