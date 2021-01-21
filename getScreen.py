import numpy as np
from PIL import ImageGrab
import cv2
import time
from mss import mss
from presskeys import FinalDoomCommands
from presskeys_DIRECT import W,A,S,D, LSHIFT, SPACE, PressKey, ReleaseKey
def random_action(doom_obj):
     e = np.random.randint(0,28)
     print(e)
     if e == 0:
        doom_obj.forward(0.5)
     elif e == 1:
        doom_obj.backward(0.5)
     elif e == 2:
        doom_obj.strafe_r(0.5)
     elif e == 3:
        doom_obj.strafe_l(0.5)
     elif e == 4:
        doom_obj.interact()
     elif e == 5: 
        doom_obj.run_modifier('on')
     elif e == 7: 
        doom_obj.run_modifier('off')
     elif e == 8:
        doom_obj.look_right()
     elif e == 9:
        doom_obj.look_left()
     elif e == 10: 
        doom_obj.fire('pistol')
     elif e == 11:
        doom_obj.fire('c_shotgun')
     elif e == 12:
        doom_obj.fire('s_shotgun')
     elif e == 13:
        doom_obj.fire('minigun')
     elif e == 14:
        doom_obj.fire('launcher')
     elif e == 15:
        doom_obj.fire('plasma')
     elif e == 16:
        doom_obj.fire('BFG')
     elif e == 17:
        doom_obj.fire('knuckles')
     elif e == 18:
        doom_obj.fire('chainsaw')
     elif e == 19:
        doom_obj.switch_wep('pistol')
     elif e == 20:
        doom_obj.switch_wep('shotgun')
     elif e == 21:
        doom_obj.switch_wep('shotgun')
        doom_obj.switch_wep('shotgun')
     elif e == 22:
        doom_obj.switch_wep('minigun')
     elif e == 23:
        doom_obj.switch_wep('launcher')
     elif e == 24:
        doom_obj.switch_wep('plasma')
     elif e == 25:
        doom_obj.switch_wep('BFG')
     elif e == 26:
        doom_obj.switch_wep('melee')

def screen_record_new(doom_obj): 
    monitor = {"top": 40, "left": 0, "width": 900, "height": 800}            # 1000x800 windowed mode
    with mss() as sct:
        while(True):
            last_time = time.time()
            #random_action(doom_obj)
            # PressKey(W)
            # PressKey(LSHIFT)
            doom_obj.forward()
           # img = np.asarray(sct.grab(monitor))#printscreen =  np.array(ImageGrab.grab(bbox=(2,40,1000,800))) #this is the old inefficient way with PIL.ImageGrab.grab 
            img =  np.array(ImageGrab.grab(bbox=(2,40,1000,800)))
            print('fps: {0}'.format(1/(time.time()-last_time))) #time.time() - last_time is seconds for each frame, 1/this is fps. 
            cv2.imshow('test_window',cv2.cvtColor(img, cv2.COLOR_BGRA2BGR))
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break

def main():
    doom_obj = FinalDoomCommands()
    for i in list(range(3))[::-1]:
        print(i+1)
        time.sleep(1)
    doom_obj.pause_toggle()
    screen_record_new(doom_obj)
    # for i in list(range(50)):
    #     print(i)
    #     random_action(doom_obj)
    #screen_record_new(doom_obj)
    doom_obj.pause_toggle()
main()