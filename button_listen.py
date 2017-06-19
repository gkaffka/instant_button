from gpiozero import Button
import os

button = Button(2)
button_ = Button(3)
needUpdate = True

while True:
    if button.is_pressed:
        os.system("mpg123 /home/pi/Downloads/sound.mp3")
        if needUpdate:
            os.system("curl -L -o /home/pi/instant_button/sound.mp3 https://github.com/gkaffka/instant_button/raw/master/sound.mp3")
            needUpdate = False

    if button_.is_pressed:
        os.system("cd /home/pi/instant_button/ && git pull")
