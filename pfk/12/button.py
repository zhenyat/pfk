#!/usr/bin/env python3
################################################################################
#   button.py
#
#   <Executable Module Purpose>
#
#   16.06.2017  Created by:  zhenya
################################################################################

from tkinter import *

def say_hello():
  print('Hello')

tk = Tk()
btn = Button(tk, text="click me", command=say_hello)
btn.pack()

tk.mainloop()