# from tkinter import Label
# widget = Label(None, text='Hello GUI world!')
# widget.pack()
# widget.mainloop()

'''
1. (expand=YES, fill=BOTH): ensures the text remains in the center.
-->expand=YES option
Asks the packer to expand the allocated space for the widget in general into any
unclaimed space in the widget’s parent.
-->fill option
Can be used to stretch the widget to occupy all of its allocated space.
'''

from tkinter import *
Label(None, text='Hello GUI world!').pack(expand=YES, fill=BOTH)
mainloop()
