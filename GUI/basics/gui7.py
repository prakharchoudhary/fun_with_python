################# ADDING MULTIPLE WIDGETS #####################

import sys
from tkinter import *

def greeting():
	print("Hello stdout world!...")

win = Frame()
win.pack()
Label(win, text='Hello container world').pack(side=TOP)
Button(win, text='Hello', command=greeting).pack(side=LEFT)
Button(win, text='Quit', command=win.quit).pack(side=RIGHT)
win.mainloop()
