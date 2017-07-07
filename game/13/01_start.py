#!/usr/bin/env python3
################################################################################
#   01_start.py
#
#   #   Python for Kids, Ch. 13: First code
#
#   07.07.2017  Created by:  zhenya
################################################################################

from   tkinter import *
import random
import time

tk = Tk()
tk.title("Game")
tk.resizable(0, 0)                # Set fixed size Window
tk.wm_attributes("-topmost", 1)   # Place Window over all other windows

canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()

tk.update()   # Initializes itsekf for teh game animation

tk.mainloop()