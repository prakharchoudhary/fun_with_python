######################### CUSTOMISED BUTTONS #######################

import sys
from tkinter import *

class ThemedButton(Button):
	def __init__(self, parent=None, **configs):
		Button.__init__(self, parent, **configs)
		self.pack()
		self.config(fg='red', bg='black', font=('courier', 12), relief=RAISED, bd=5)

B1 = ThemedButton(text='spam', command=onSpam)
B2 = ThemedButton(text='eggs')
B2.pack(expand=YES, fill=BOTH)
