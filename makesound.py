import tkinter as tk
import pygame
from pygame import mixer


mixer.init()


def play_sound():
    sound = mixer.Sound("sound.wav")  # Replace "sound.wav" with your actual sound file
    sound.play()


root = tk.Tk()
root.title("Sound Button")


button = tk.Button(root, text="Play Sound", command=play_sound)
button.pack()


root.mainloop()
