import time
import datetime
from pygame import mixer

print("""           Welcome to python program for healthy routine. 
The program reminds you to regularly drink water and regular exercise""")


def music(key):
    mixer.init()  # Starting the mixer
    mixer.music.load(f"{key}")  # Loading the song
    mixer.music.set_volume(0.7)  # Setting the volume
    mixer.music.play()  # Start playing the song

    x = input("type done after completing the task")
    if x == "done" or x == "Done" or x == "DONE":
        # stopping the song
        mixer.music.pause()


def wat():
    music(darkside.mp3)


def phy():
    music(end_of_time.mp3)


def eye():
    music(unity.mp3)
