#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from Tkinter import *
from tkMessageBox import showinfo

def reply(name):
    showinfo(title='Reply', message='Hello %s!' % name)

top = Tk()
top.title('Echo')

Label(top, text='Enter your name:').pack(side=TOP)
ent = Entry(top)
ent.pack(side=TOP)
btn = Button(top, text='Submit', command=(lambda: reply(ent.get())))
btn.pack(side=LEFT)

top.mainloop()
