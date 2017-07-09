#!/usr/bin/env python3
################################################################################
#   08_paddle_class.py
#
#   Python for Kids, Ch. 14 a paddle class
#
#   08.07.2017  Created by:  zhenya
################################################################################

from   tkinter import *
import random
import time

class Ball:
  def __init__(self, canvas, color):
    self.canvas = canvas
    self.id     = canvas.create_oval(10, 10, 25, 25, fill=color)  # 10,10 - top-left
                                                                  # 25,25 - bottom-right
    self.canvas.move(self.id, 245, 100)   # move to middle of canvas (not good code)
    
    starts = [-3, -2, -1, 1, 2, 3]
    random.shuffle(starts)
    self.x =  starts[0]
    self.y = -3
    self.canvas_height = self.canvas.winfo_height()
    self.canvas_width  = self.canvas.winfo_width()
    
  def draw(self):                   # 05: change code below
    self.canvas.move(self.id, self.x, self.y)

    # current position: [top-left-x, top-left-y, bottom-right-x, bottom-right-y]
    pos = self.canvas.coords(self.id) # current position

    if pos[1] <= 0:                   # Top reached
      self.y = 3
    if pos[3] >= self.canvas_height:  # Bottom reached
      self.y = -3
    if pos[0] <= 0:                   # Left reached
      self.x = 3
    if pos[2] >= self.canvas_width:   # Rightreached
      self.x = -3
# 08
class Paddle:
  def __init__(self, canvas, color):
    self.canvas = canvas
    self.id     = canvas.create_rectangle(0, 0, 100, 10, fill=color)
    self.canvas.move(self.id, 200, 300)

  def draw(self):
    pass

tk = Tk()
tk.title("Game")
tk.resizable(0, 0)                # Set fixed size Window
tk.wm_attributes("-topmost", 1)   # Place Window over all other windows

canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()

tk.update()   # Initializes itsekf for teh game animation

ball   = Ball(canvas, 'red')
paddle = Paddle(canvas, 'blue') # 08

# Main loop:  redraws screen
while(True):
  ball.draw()
  paddle.draw()           # 08
  tk.update_idletasks()
  tk.update()
  time.sleep(0.01)


tk.mainloop()