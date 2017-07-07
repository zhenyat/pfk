#!/usr/bin/env python3
################################################################################
#   rectangles.py
#
#   Python for Kids, Ch. 12: Tkinter a lot of rectangles
#
#   05.07.2017  Created by:  zhenya
################################################################################

from tkinter import *
import random

tk     = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()

def random_rectangle(width, height):
  x1 = random.randrange(width)
  y1 = random.randrange(height)
  x2 = x1 + random.randrange(width)
  y2 = y1 + random.randrange(height)
  canvas.create_rectangle(x1, y1, x2, y2)

for x in range(0, 100):
  random_rectangle(400, 400)

def random_rectangle_colored(width, height, color):
  x1 = random.randrange(width)
  y1 = random.randrange(height)
  x2 = x1 + random.randrange(width)
  y2 = y1 + random.randrange(height)
  canvas.create_rectangle(x1, y1, x2, y2, fill=color)

random_rectangle_colored(200, 200, 'green')

tk.mainloop()