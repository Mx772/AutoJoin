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

# Do whatever array of words you want to process here. Using 'left the game' works, but then you may get false-positives when there isn't room in the server. 
giveaways = ['left the game']

def autoJoin(): 
	time.sleep(2)
	print('Waiting to Join Game')
	# Path of tesseract executable 
	# Example: `C:\Users\myPC\Documents\Tesseract-OCR\tesseract.exe`
	pytesseract.pytesseract.tesseract_cmd =r'C:\Program Files\Tesseract-OCR\tesseract.exe'
	while(True): 
		cap = ImageGrab.grab(all_screens=True, bbox =(2840, 1727, 3780, 1850))
		tesstr = pytesseract.image_to_string(cap, lang ='eng')
		keyboard = Controller()
		if any(word in tesstr for word in giveaways):
			print("Found!")
			mcWin = gw.getWindowsWithTitle('Minecraft')[0]
			mcWin.activate()
			keyboard.press(Key.enter)
			keyboard.release(Key.enter)
			# Uncomment to play sound
			# playsound('G:\\Downloads\\1_second_tone.mp3')
			quit()

autoJoin() 

