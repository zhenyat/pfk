#!/usr/bin/env python3
################################################################################
#   07_ball_direction.py
#
#   Python for Kids, Ch. 13: a ball direction (x limits)
#
#   07.07.2017  Created by:  zhenya
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
    self.canvas_width  = self.canvas.winfo_width()    # 07
    
  def draw(self):                   # 05: change code below
    self.canvas.move(self.id, self.x, self.y)

    # current position: [top-left-x, top-left-y, bottom-right-x, bottom-right-y]
    pos = self.canvas.coords(self.id) # current position

    if pos[1] <= 0:                   # Top reached
      self.y = 3
    if pos[3] >= self.canvas_height:  # Bottom reached
      self.y = -3
    # 07
    if pos[0] <= 0:
      self.x = 3
    if pos[2] >= self.canvas_width:
      self.x = -3
    
tk = Tk()
tk.title("Game")
tk.resizable(0, 0)                # Set fixed size Window
tk.wm_attributes("-topmost", 1)   # Place Window over all other windows

canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()

tk.update()   # Initializes itsekf for teh game animation

ball = Ball(canvas, 'red')

# Main loop:  redraws screen
while(True):
  ball.draw()     
  tk.update_idletasks()
  tk.update()
  time.sleep(0.01)


tk.mainloop()