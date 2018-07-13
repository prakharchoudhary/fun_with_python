################### ADDING TITLE ##########################

from tkinter import *
root = Tk()
widget = Label(root)
widget.config(text='Hello GUI world!')
widget.pack(side=TOP, expand=YES, fill=BOTH)
root.title('Hello')
root.mainloop()

'''MINIMALISTIC CODE
from tkinter import *
Label(None, {'text': 'Hello GUI world!', Pack: {'side': 'top', expand: 'yes', fill: 'both'}}).mainloop()
'''
