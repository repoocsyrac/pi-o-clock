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

def check_alarms():
    now = datetime.now()
    for alarm in alarms:
        if now.hour == alarm['hour'] and now.minute == alarm['minute']:
            play_alarm(alarm['sound'])
    root.after(60000, check_alarms)  # Check every minute

    
pygame.mixer.init()

root = tk.Tk()
root.title("Pi-o-Clock")
root.geometry("480x320")

alarms = []  # List to store alarm times and sounds

time_label = tk.Label(root, text="", font=("Helvetica", 48))
time_label.pack(expand=True)

update_time()
root.mainloop()