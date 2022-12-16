# Tkinter-music-box
#Import
from tkinter import *
from glob import glob
import os

#Base
root=Tk()
root.title('Music box')
root.attributes('-fullscreen', True)

#Play song
def play():
    song=song_box.get(ACTIVE)
    os.system('path of your folder'+song+".mp3")

#Set song box
song_box=Listbox(root,bg='black',font=('Kaiti',28),fg='white',width=60)
song_box.pack(pady=20)

#Find song
gb=glob('path of your folder + *.mp3')
x=len(gb)

#Modify song
y=0
for i in range(x):
    gb[y]=gb[y].replace('path of your folder + \\','')
    gb[y]=gb[y].replace('.mp3','')
    y+=1

#Insert song
y=0
for i in range(x):
    song_box.insert(x,gb[y])
    y+=1

#Set button
play_button = Button(root, text="Play Song", font=("Times", 28), relief=GROOVE, command=play)
play_button.pack(pady=20)
exit = Button(root, text="Exit", font=("Times", 22), relief=GROOVE, command=exit)
exit.pack(pady=18)

#Start
root.mainloop()
