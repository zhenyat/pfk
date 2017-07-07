#!/usr/bin/env python3
################################################################################
#   button.py
#
#   Python for Kids, Ch. 12: Tkinter button
#
#   16.06.2017  Created by:  zhenya
#   05.06.2017  Last update (comments)
################################################################################

from tkinter import *

def say_hello():
  print('Hello')

tk = Tk()                                             # Object of class Tk 
                                                      # creates a basic window
btn = Button(tk, text="click me", command=say_hello)  # creates button with named parameters
                                                      # added to window
btn.pack()                                            # displays button

tk.mainloop()