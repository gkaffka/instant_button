import os, threading, time


counter = 0
for i in temp:
    command = "curl -L -o {}.mp3 https://www.myinstants.com/media/sounds/{}".format( counter, i)
    os.system(command)
    counter += 1