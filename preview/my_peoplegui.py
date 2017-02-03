#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from Tkinter import *
from tkMessageBox import showerror
import shelve

db_name = 'people-class'
fieldnames = ('name', 'age', 'job', 'pay')

def makeWidget():
    global entries
    window = Tk()
    window.title('People Shelve')
    form = Frame(window)
    form.pack()
    entries = {}
    for ix, label in enumerate(('key',) + fieldnames):
        lab = Label(form, text=label)
        ent = Entry(form)
        lab.grid(row=ix, column=0)
        ent.grid(row=ix, column=1)
        entries[label] = ent
    Button(window, text='Fetch', command=fetchRecord).pack(side=LEFT)
    Button(window, text='Update', command=updateRecord).pack(side=LEFT)
    Button(window, text='Quit', command=window.quit).pack(side=RIGHT)
    return window

def fetchRecord():
    key = entries['key'].get()
    try:
        record = db[key]
    except:
        showerror(title='Error', message='No Such Key!')
        # 清除相关信息
        for field in fieldnames:
            entries[field].delete(0, END)
    else:
        for field in fieldnames:
            entries[field].delete(0, END)
            entries[field].insert(0, repr(getattr(record, field)))

def updateRecord():
    key = entries['key'].get()
    try:
        record = db[key]
    except:
        # 必须针对非法输入添加错误处理
        from person import Person
        record = Person('?', '?')
    for field in fieldnames:
        setattr(record, field, eval(entries[field].get()))
    db[key] = record


db = shelve.open(db_name)

if __name__ == "__main__":
    window = makeWidget()
    window.mainloop()
