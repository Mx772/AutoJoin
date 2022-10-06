# AutoJoin
 
This is a simple Python script to auto join a Minecraft server that is full. 

The expectation here is that you set the bbox (Bounding Box) coords to a status provider of the server, such as discord if the server is using a discord bot to notify of messages/achievements/join/leave. 

## Installation
```
pip install time pynput pygetwindow pillow
```
optional:

```
pip install playsound
```

Download [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) and point `pytesseract.pytesseract.tesseract_cmd` at the install location. 

Then you would just run it via `py ./path/to/file/main.py`.

## Flow
The expected flow is for you to have the minecraft game currently up, and the server selected on the multiplayer server window. After doing that, you can then un-focus the minecraft window. 

When the program detects the words in the word array, it will then automatically focus the minecraft window (Assuming it has the name `Minecraft` in it), then click enter. This should auto join the server. 

In personal tests, this beats out almost everyone manually joining. 

## Tips

### Getting Coords
I personally use ShareX which displays the coordinates on the screen when using 'Region Capture'.

You can then put those into the bounding Box.

![image](https://user-images.githubusercontent.com/9059161/194331708-2c571644-f2ad-4855-a1f7-c7ba22a84ccb.png)


### Enabling Sound
I enable the sound toggle if I am going to do other things while waiting. This will play whatever sound you define when you are joining the game. 

Note: If you don't want sound, or don't want to grab the sound package, just comment out any lines with `playsound`.
