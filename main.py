# Used to play sounds on alert
from playsound import playsound
# Image Reading
import pytesseract 
# Image Processing
import time
# Keyboard Controller
from pynput.keyboard import Key, Controller
# Makes Minecraft Active
import pygetwindow as gw
from PIL import ImageGrab 

# Config Section:
# Insert whatever array of words you want to process here. Using 'left the game' works, but then you may get false-positives when there isn't room in the server. 
triggerList = ['left the game']
# Path of tesseract executable 
pyPath = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
soundEnabled = False
soundPath = 'G:\\Downloads\\1_second_tone.mp3'
boundingBox = (2840, 1727, 3780, 1850)

def autoJoin(): 
	time.sleep(2)
	print('Waiting to Join Game')
	pytesseract.pytesseract.tesseract_cmd = pyPath
	while(True): 
		cap = ImageGrab.grab(all_screens=True, bbox = boundingBox)
		tesstr = pytesseract.image_to_string(cap, lang ='eng')
		keyboard = Controller()
		if any(word in tesstr for word in triggerList):
			print("Found!")
			try:
				mcWin = gw.getWindowsWithTitle('Minecraft')[0]
				mcWin.activate()
				keyboard.press(Key.enter)
				keyboard.release(Key.enter)
				if soundEnabled:	
					# Uncomment to play sound
					print("Playing Sound")
					# playsound(soundPath)
			except:
				print('Could not find any windows named Minecraft')
			quit()

autoJoin() 

