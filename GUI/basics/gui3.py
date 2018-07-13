################# ADDING BUTTONS AND CALLBACKS ####################

import sys
from tkinter import *
widget = Button(None, text='Hi', command=sys.exit)
widget.pack()
widget.mainloop()