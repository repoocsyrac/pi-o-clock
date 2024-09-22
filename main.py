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

def open_alarm_setting():
    setting_window = tk.Toplevel(root)
    setting_window.title("Set Alarm")

    hour_var = tk.StringVar(value="06")  # Default to 6:30 AM
    minute_var = tk.StringVar(value="30")
    sound_var = tk.StringVar(value="default.wav")

    tk.Label(setting_window, text="Hour").pack()
    tk.Entry(setting_window, textvariable=hour_var).pack()
    
    tk.Label(setting_window, text="Minute").pack()
    tk.Entry(setting_window, textvariable=minute_var).pack()

    tk.Label(setting_window, text="Alarm Sound").pack()
    tk.Entry(setting_window, textvariable=sound_var).pack()

    def save_alarm():
        hour = int(hour_var.get())
        minute = int(minute_var.get())
        sound = sound_var.get()
        add_alarm(hour, minute, sound)
        setting_window.destroy()

    tk.Button(setting_window, text="Save", command=save_alarm).pack()

    setting_window.mainloop()




pygame.mixer.init()

root = tk.Tk()
root.title("Pi-o-Clock")
root.geometry("480x320")

alarms = []  # List to store alarm times and sounds

time_label = tk.Label(root, text="", font=("Helvetica", 48))
time_label.pack(expand=True)

update_time()
root.mainloop()