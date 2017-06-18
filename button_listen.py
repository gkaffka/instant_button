from gpiozero import Button
import os

button = Button(2)
needUpdate = True

while True:
    button.wait_for_press()
    os.system("mpg123 /home/pi/Downloads/sound.mp3")
    if needUpdate:
        os.system("curl -L -o /home/pi/Downloads/sound.mp3 https://github.com/gkaffka/instant_button/raw/master/sound.mp3")
        needUpdate = False
