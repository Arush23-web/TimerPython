import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import time
import threading


def run_timer(minutes, progress_bar, time_label):
    total_seconds = minutes * 60
    for second in range(total_seconds + 1):
        minutes_left = (total_seconds - second) // 60
        seconds_left = (total_seconds - second) % 60
        time_str = f"{minutes_left:02}:{seconds_left:02}"
        time_label.config(text=f"Time Left: {time_str}")

        progress_bar['value'] = (second / total_seconds) * 100

        time.sleep(1)

    time_label.config(text="Time's up! Great job!")
    progress_bar['value'] = 100


def start_timer(minutes, progress_bar, time_label):
    timer_thread = threading.Thread(target=run_timer, args=(minutes, progress_bar, time_label))
    timer_thread.start()


def create_timer_window(minutes):
    window = tk.Tk()
    window.title("Study Timer")
    window.geometry("1920x1080")

    bg_image = Image.open("timerbg.jpg")
    bg_image = bg_image.resize((1920, 1080), Image.Resampling.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    bg_label = tk.Label(window, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    time_label = tk.Label(window, text="Time Left: 00:00", font=("Helvetica", 24), fg="white", bg="#282c34")
    time_label.pack(pady=20)

    progress_bar = ttk.Progressbar(window, orient="horizontal", length=300, mode="determinate")
    progress_bar.pack(pady=10)

    start_timer(minutes, progress_bar, time_label)

    window.mainloop()


create_timer_window(60)
#Inspired from other youtube channels.
