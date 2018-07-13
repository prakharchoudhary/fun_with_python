############ USER DEFINED CALLBACKS #################

import sys
from tkinter import *

def quit():
	print("Hello, I must be going.")
	sys.exit()

widget = Button(None, text='Hello event world', command=quit)
widget.pack()
widget.mainloop()