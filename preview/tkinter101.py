#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from Tkinter import *
from tkMessageBox import showinfo
#from tkinter.messagebox import showinfo

def reply():
    showinfo(title='popup', message='Button pressed!')

window = Tk()
btn = Button(window, text='press', command=reply)

btn.pack()
window.mainloop()
