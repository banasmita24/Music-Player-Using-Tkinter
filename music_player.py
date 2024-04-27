from tkinter import *
import tkinter as tk
from tkinter import ttk, filedialog
from pygame import mixer
import os

root = Tk()
root.title("Music Player")
root.geometry("920x670+290+85")
root.configure(background="#0f1a2b")
root.resizable(width=False, height=False)

mixer.init()

def open_folder():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)
        for song in songs:
            if song.endswith(".mp3"):
                playlist.insert(END, song)

def play_song():
    music_name=playlist.get(ACTIVE)
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()
    music.config(text=music_name[0:-4])

def set_volume(val):
    volume = float(val) / 100
    mixer.music.set_volume(volume)

class VolumeSlider(tk.Scale):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.config(orient=HORIZONTAL, showvalue=TRUE, command=set_volume, troughcolor="lightgrey", bg="silver")

        # Set initial volume
        self.set(50)

#icon
image_icon = PhotoImage(file="logo.png")
root.iconphoto(False, image_icon)

#Top
Top = PhotoImage(file="top.png")
Label(root, image=Top, background="#0f1a2b").pack()

#logo
Logo = PhotoImage(file="logo.png")
Label(root, image=Logo, background="#0f1a2b").place(x=65, y=115)

#button
play_button = PhotoImage(file="play.png")
Button(root, image=play_button, background="#0f1a2b", bd=0, command=play_song).place(x=100, y=400)

stop_button = PhotoImage(file="stop.png")
Button(root, image=stop_button, background="#0f1a2b", bd=0, command=mixer.music.stop).place(x=30, y=500)

resume_button = PhotoImage(file="resume.png")
Button(root, image=resume_button, background="#0f1a2b", bd=0, command=mixer.music.unpause).place(x=115, y=500)

pause_button = PhotoImage(file="pause.png")
Button(root, image=pause_button, background="#0f1a2b", bd=0, command=mixer.music.pause).place(x=200, y=500)

#label
music = Label(root, text="", font=("Arial", 15), fg="white", background="#0f1a2b")
music.place(x=150, y=340, anchor="center")

#music
Menu = PhotoImage(file="menu.png")
Label(root, image=Menu, background="#0f1a2b").pack(padx=10, pady=50, side=RIGHT)

#volume
volume_frame = Frame(root, background="#0f1a2b")
volume_frame.place(x=50, y=600)

volume_label = Label(volume_frame, text="Volume: ", font=("Arial", 12), fg="white", background="#0f1a2b")
volume_label.pack(side=LEFT)

volume_slider = VolumeSlider(volume_frame, width=20)
volume_slider.pack(side=LEFT, fill=X)

#music frame
music_frame = Frame(root, bd=2, relief=RIDGE)
music_frame.place(x=330, y=350, width=560, height=250)

Button(root, text="Open Folder", width=15, height=2, bg="darkgoldenrod", fg="white", command=open_folder, font=("Arial", 10, "bold")).place(x=330, y=300)

scroll = Scrollbar(music_frame)
playlist = Listbox(music_frame, width=100, font=("Arial", 10), background="#333333", fg="white", selectbackground="crimson", cursor="hand2", bd=0, yscrollcommand=scroll.set)
scroll.pack(side=RIGHT, fill=Y)
playlist.pack(side=LEFT, fill=BOTH)
scroll.config(command=playlist.yview)

root.mainloop()