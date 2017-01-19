#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from Tkinter import mainloop
from tkMessageBox import showinfo
from tkinter102 import MyGui

class CustomGui(MyGui):
    def reply(self):
        showinfo(title='popup', message='Ouch!')


if __name__ == "__main__":
    CustomGui().pack()
    mainloop()
