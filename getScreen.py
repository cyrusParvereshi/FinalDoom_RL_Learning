import numpy as np
from PIL import ImageGrab
import cv2
import time
from mss import mss
# just so this doesn't go on forever:

def screen_record_new(): 
    monitor = {"top": 40, "left": 0, "width": 900, "height": 800}
    with mss() as sct:
        while(True):
            # 1000x800 windowed mode
            last_time = time.time()
            img = np.asarray(sct.grab(monitor))#printscreen =  np.array(ImageGrab.grab(bbox=(2,40,1000,800))) #this is the old inefficient way with PIL.ImageGrab.grab 
            print('fps: {0}'.format(1/(time.time()-last_time))) #time.time() - last_time is seconds for each frame, 1/this is fps. 
            cv2.imshow('test_window',cv2.cvtColor(img, cv2.COLOR_BGRA2BGR))
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break
screen_record_new()