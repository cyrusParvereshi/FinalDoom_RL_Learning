import pyautogui
import time
import autoit
class GeneralCommands: 
	'''Commands that are more or less universal to any game '''
	def __init__(self):
		self.User = 'Cyrus'
		#pyautogui.PAUSE = 0.2

	def forward(self, secs=1): 
		pyautogui.keyDown('w') 
		#time.sleep(secs)
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
		self.reset_mouse() #recenter mouse to center of game screen on left side

	def interact(self):
		pyautogui.keyDown('space') #might want to change to 'e'. 
		time.sleep(0.5)
		pyautogui.keyUp('space')

	def run_modifier(self, toggle ='on'):
		if toggle == 'on': 
			pyautogui.keyDown('shiftleft')
		if toggle == 'off':
			pyautogui.keyUp('shiftleft')

	def look_right(self, secs=0.5):  #might want to replace these with more smooth mouse functions 
		pyautogui.keyDown('right')
		time.sleep(secs)
		pyautogui.keyUp('right')

	def look_left(self, secs=0.5):
		pyautogui.keyDown('left')
		time.sleep(secs)
		pyautogui.keyUp('left')

	def reset_mouse(self):
		pyautogui.moveTo(x=466, y=340)

	def pause_toggle(self):
		pyautogui.press('esc')

	def fire(self, wep_name='c_shotgun'):	
		print(f"firing {wep_name}")
		if wep_name == 'pistol': #Should consider new method for continous fire weapons
		    firing_time = 0.1
		    cooldown_time = 0.5#0.01
		elif wep_name == 'c_shotgun': #combat shotgun
		    firing_time = 0.8
		    cooldown_time = 0.02
		elif wep_name == 's_shotgun': #super shotgun
		    firing_time = 0.2
		    cooldown_time = 1.5
		elif wep_name == 'minigun':
			firing_time = 0.1
			cooldown_time = 0.2
		elif wep_name == 'launcher': #rocket launcher
		    firing_time = 0.1
		    cooldown_time = 0.5
		elif wep_name == 'plasma': #plasma rifle
			firing_time = 0.1
			cooldown_time = 0.8 
		elif wep_name == 'BFG': #BFG-9000
			firing_time = 0.05
			cooldown_time = 1.5
		elif wep_name == 'knuckles': #basic melee weapon
			firing_time = 0.2
			cooldown_time = 0.4
		elif wep_name == 'chainsaw': #chainsaw (on pressing 1 is switched to first before knuckles)
			firing_time = 0.05 
			cooldown_time = 0.1
		else:
			print('invalid weapon')
			return
		#different weapons have different firing times
		pyautogui.keyDown('ctrl') #can also map to a mousedown thing if necessary
		time.sleep(firing_time)
		pyautogui.keyUp('ctrl')
		time.sleep(cooldown_time)

	def switch_wep(self,wep_name = 'shotgun'):
		if wep_name == 'pistol': #Should consider new method for continous fire weapons
		   pyautogui.keyDown('2')
		   pyautogui.keyUp('2')
		elif wep_name == 'shotgun': #combat shotgun AND super shotgun, must press twice to toggle
			pyautogui.keyDown('3')
			pyautogui.keyUp('3') 
		elif wep_name == 'minigun':
			pyautogui.keyDown('4')
			pyautogui.keyUp('4')
		elif wep_name == 'launcher': #rocket launcher
			pyautogui.keyDown('5')
			pyautogui.keyUp('5')
		elif wep_name == 'plasma': #plasma rifle
			pyautogui.keyDown('6')
			pyautogui.keyUp('6')
		elif wep_name == 'BFG':
			pyautogui.keyDown('7')
			pyautogui.keyUp('7')
		elif wep_name == 'melee': #toggles between chainsaw and knuckles
			pyautogui.keyDown('1')
			pyautogui.keyUp('1')
		else:
			print('invalid weapon')
		time.sleep(1) #weapon switch time is about 1 second



if __name__ == '__main__':
	print("providing inputs in: ") #
	for i in list(range(3))[::-1]:
	    print(i+1)
	    time.sleep(1)
	doom_obj = FinalDoomCommands()
	doom_obj.pause_toggle()
	doom_obj.look_right(0.1)
	doom_obj.look_left(0.5)
	doom_obj.forward()
	doom_obj.backward()
	doom_obj.strafe_r()
	doom_obj.strafe_l(0.3)
	doom_obj.run_modifier('on')
	doom_obj.forward()
	doom_obj.run_modifier('off') #if don't turn off will hold shift after program ended
	doom_obj.strafe_r()
	doom_obj.run_modifier('on')
	doom_obj.forward(2)
	doom_obj.interact()
	doom_obj.forward(1)
	doom_obj.run_modifier('off')
	doom_obj.switch_wep('pistol')
	doom_obj.fire('pistol')
	doom_obj.switch_wep('shotgun')
	doom_obj.fire('s_shotgun')
	doom_obj.switch_wep('shotgun')
	doom_obj.fire('c_shotgun')
	doom_obj.switch_wep('minigun')
	doom_obj.fire('minigun')
	doom_obj.switch_wep('launcher')
	doom_obj.fire('launcher')
	doom_obj.switch_wep('plasma')
	doom_obj.fire('plasma')
	doom_obj.switch_wep('BFG')
	doom_obj.fire('BFG')
	doom_obj.switch_wep('melee')
	doom_obj.fire('chainsaw')
	doom_obj.switch_wep('melee')
	doom_obj.fire('knuckles')



	doom_obj.pause_toggle()