#!/usr/bin/env python3
################################################################################
#   8_animation.py
#
#   Python for Kids, Ch. 12: Tkinter basic animation
#
#   06.07.2017  Created by:  zhenya
################################################################################

import time
from tkinter import *

tk     = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()

canvas.create_polygon(10, 10, 10, 60, 50, 35, fill='red')   # id = 1

for x in range(0, 60):
  canvas.move(1, 5, 0)  # moves object with id=1 5px across and 0px down
  tk.update()           # redraw the screen 
  time.sleep(0.05)
  
canvas.create_polygon(10, 10, 10, 60, 50, 35)   # id = 2
for x in range(0, 60):
  canvas.move(2, 5, 5)
  tk.update()
  time.sleep(0.05)
  
for x in range(0, 60):
  canvas.move(2, -5, -5)
  tk.update()
  time.sleep(0.05)

canvas.itemconfig(2, fill='blue', outline='red')

id = canvas.create_polygon(10, 10, 10, 60, 50, 35, fill='green')
for x in range(0, 60):
  canvas.move(id, 0, 5)
  tk.update()
  time.sleep(0.05)

tk.mainloop()
