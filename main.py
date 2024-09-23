import tkinter as tk
import tkinter.filedialog
from datetime import datetime
import pygame

def update_time():
    now = datetime.now().strftime("%H:%M:%S")
    time_label.config(text=now)
    root.after(1000, update_time)

def add_alarm(hour, minute, sound):
    alarms.append({"hour": hour, "minute": minute, "sound": sound, "has_rung": False})

def play_alarm(sound_file):
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play(loops=-1) # Loops until stopped by user

def stop_alarm():
    pygame.mixer.music.stop()

def check_alarms():
    now = datetime.now()
    for alarm in alarms:
        if now.hour == alarm['hour'] and now.minute == alarm['minute'] and not alarm['has_rung']:
            play_alarm(alarm['sound'])
            alarm['has_rung'] = True
    root.after(1000, check_alarms)  # Check every second

def open_alarm_setting():
    setting_window = tk.Toplevel(root)
    setting_window.title("Set Alarm")

    hour_var = tk.StringVar(value="06")  # Default to 6:30 AM
    minute_var = tk.StringVar(value="30")
    sound_var = tk.StringVar(value="default.wav")

    tk.Label(setting_window, text="Hour").pack(pady=5, padx=50)
    tk.Entry(setting_window, textvariable=hour_var).pack(padx=50)
    
    tk.Label(setting_window, text="Minute").pack(pady=5, padx=50)
    tk.Entry(setting_window, textvariable=minute_var).pack(padx=50)

    tk.Label(setting_window, text="Alarm Sound").pack(pady=5, padx=50)
    tk.Entry(setting_window, textvariable=sound_var).pack(padx=50)

    # Function to select a custom sound file
    def choose_custom_sound():
        file_path = tk.filedialog.askopenfilename(title="Select Alarm Sound", filetypes=[("Sound files", "*.mp3 wav")])
        if file_path:
            sound_var.set(file_path)
        setting_window.grab_set()
        setting_window.focus_force()

    tk.Button(setting_window, text="Choose Sound", command=choose_custom_sound).pack(pady=5)

    def save_alarm():
        hour = int(hour_var.get())
        minute = int(minute_var.get())
        sound = sound_var.get()
        add_alarm(hour, minute, sound)
        update_alarm_list()
        setting_window.destroy()

    tk.Button(setting_window, text="Save", command=save_alarm).pack(pady=10, padx=10)

    setting_window.mainloop()

def update_alarm_list():
    for widget in alarm_list_frame.winfo_children():
        widget.destroy()  # Clear old list

    for alarm in alarms:
        alarm_str = f"{alarm['hour']:02d}:{alarm['minute']:02d} - {alarm['sound']}"
        label = tk.Label(alarm_list_frame, text=alarm_str)
        label.pack()

        def delete_alarm(a=alarm):
            alarms.remove(a)
            update_alarm_list()

        tk.Button(alarm_list_frame, text="Delete", command=delete_alarm).pack()

# Init pygame mixer for sound
pygame.mixer.init()

# Main window
root = tk.Tk()
root.title("Pi-o-Clock")
root.geometry("480x320")

# List to store alarm times and sounds
alarms = []

# UI Elements
time_label = tk.Label(root, text="", font=("Helvetica", 48))
time_label.pack(expand=True)
set_alarm_button = tk.Button(root, text="Set Alarm", command=open_alarm_setting, font=("Helvetica", 16))
set_alarm_button.pack(pady=10)
alarm_list_frame = tk.Frame(root)
alarm_list_frame.pack()
stop_alarm_button = tk.Button(root, text="Stop Alarm", command=stop_alarm, font=("Helvetica", 16))
stop_alarm_button.pack(pady=10)

# Start updating the clock
update_time()
# Start checking for alarms
check_alarms()

root.mainloop()