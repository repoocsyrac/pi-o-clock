import tkinter as tk
from datetime import datetime
import pygame

def update_time():
    now = datetime.now().strftime("%H:%M:%S")
    time_label.config(text=now)
    root.after(1000, update_time)

def add_alarm(hour, minute, sound):
    alarms.append({"hour": hour, "minute": minute, "sound": sound})

def play_alarm(sound_file):
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()
    
pygame.mixer.init()

root = tk.Tk()
root.title("Pi-o-Clock")
root.geometry("480x320")

alarms = []  # List to store alarm times and sounds

time_label = tk.Label(root, text="", font=("Helvetica", 48))
time_label.pack(expand=True)

update_time()
root.mainloop()