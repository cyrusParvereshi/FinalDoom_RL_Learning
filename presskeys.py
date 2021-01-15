import pyautogui
import time
import autoit
class GeneralCommands: 
	'''Commands that are more or less universal to any desktop game '''
	def __init__(self):
		self.User = 'Cyrus'
		#pyautogui.PAUSE = 0.2

	def forward(self, secs=1): 
		pyautogui.keyDown('w') 
		time.sleep(secs)
		pyautogui.keyUp('w')

	def backward(self, secs = 1): 
		pyautogui.keyDown('s')
		time.sleep(secs)
		pyautogui.keyUp('s')

	def strafe_r(self, secs=1):
		pyautogui.keyDown('d')
		time.sleep(secs)
		pyautogui.keyUp('d')

	def strafe_l(self, secs=1): 
		pyautogui.keyDown('a')
		time.sleep(2)
		pyautogui.keyUp('a')

class FinalDoomCommands(GeneralCommands):
	'''commands specific to FINAL DOOM and other 1990s DOOM games.
	NOTE: you may want to change the interact() function to "E" instead as that is sometimes what 
	your version will use. Space is interact in the Steam version of Final Doom. '''
	def __init__(self):
		super().__init__()
		self.mission = 'TNT' #can be changed to 'Plutonia' for FinalDoom, can hold episode for UltimateDoom. 
		self.level = 1 #can be used to keep track of which level you running on. 

	def interact(self):
		pyautogui.keyDown('space') #might want to change to 'e'. 
		time.sleep(0.5)
		pyautogui.keyUp('space')

	def run_modifier(self, toggle ='on'):
		if toggle == 'on': 
			pyautogui.keyDown('shiftleft')
		if toggle == 'off':
			pyautogui.keyUp('shiftleft')

	def look_right(self, secs=2):  #might want to replace these with more smooth mouse functions 
		pyautogui.keyDown('right')
		time.sleep(secs)
		pyautogui.keyUp('right')

	def look_left(self, secs=2):
		pyautogui.keyDown('left')
		time.sleep(secs)
		pyautogui.keyUp('left')

	def reset_mouse(self):
		pyautogui.moveTo(x=466, y=340)

	def pause_toggle(self):
		pyautogui.press('esc')

	def fire(self, wep_name):	
		print(f"firing {wep_name}")
		if wep_name == 'pistol': #Should consider new method for continous fire weapons
		    firing_time = 0.9
		    cooldown_time = 0.5
		elif wep_name == 'c_shotgun': #combat shotgun
		    firing_time = 1.2
		    cooldown_time = 1
		elif wep_name == 's_shotgun': #super shotgun
		    firing_time = 1
		    cooldown_time = 2
		elif wep_name == 'minigun':
			firing_time = 0.5
			cooldown_time = 0.3
		elif wep_name == 'launcher': #rocket launcher
		    firing_time = 1
		    cooldown_time = 2
		elif wep_name == 'plasma': #plasma rifle
			firing_time = 0.4
			cooldown_time = 0.8 
		elif wep_name == 'BFG':
			firing_time = 2
			cooldown_time = 1
		elif wep_name == 'knuckles':
			firing_time = 1
			cooldown_time = 0.5
		elif wep_name == 'chainsaw':
			firing_time = 0.2
			cooldown_time = 0.4
		else:
			print('invalid weapon')
			return
		#click mouse
		pyautogui.mouseDown(button='left') #x=466,y=340,
		time.sleep(firing_time)
		pyautogui.mouseUp(button='left')
		time.sleep(cooldown_time)



if __name__ == '__main__':
	print("providing inputs in: ") #
	for i in list(range(3))[::-1]:
	    print(i+1)
	    time.sleep(1)
	doom_obj = FinalDoomCommands()
	doom_obj.reset_mouse() #recenter mouse to center of game screen on left side
	doom_obj.pause_toggle()
	doom_obj.look_right(0.5)
	doom_obj.look_left(0.5)
	# doom_obj.forward()
	# doom_obj.backward()
	# doom_obj.strafe_r()
	# doom_obj.strafe_l(0.3)
	# doom_obj.run_modifier('on')
	# doom_obj.forward()
	# doom_obj.run_modifier('off') #if don't turn off will hold shift after program ended

	# doom_obj.strafe_r()
	# doom_obj.run_modifier('on')
	# doom_obj.forward(2)
	# doom_obj.interact()ds
	# doom_obj.forward(1)
	# doom_obj.run_modifier('off')
	# for j in list(range(4)):
	time.sleep(1)
	doom_obj.fire('pistol')
	doom_obj.pause_toggle()