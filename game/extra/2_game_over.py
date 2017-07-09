#!/usr/bin/env python3
################################################################################
#   2_game_over.py
#
#   Python for Kids, Extra code: button
#
#   09.07.2017  Created by:  zhenya
################################################################################

from   tkinter import *
import random
import time
import sys
import os

class Ball:
  def __init__(self, canvas, paddle, color):
    self.canvas = canvas
    self.paddle = paddle
    self.id     = canvas.create_oval(10, 10, 25, 25, fill=color)  # 10,10 - top-left
                                                                  # 25,25 - bottom-right
    self.canvas.move(self.id, 245, 100)   # move to middle of canvas (not good code)
    
    starts = [-3, -2, -1, 1, 2, 3]
    random.shuffle(starts)
    self.x =  starts[0]
    self.y = -3
    self.canvas_height = self.canvas.winfo_height()
    self.canvas_width  = self.canvas.winfo_width()
    self.hit_bottom    = False

  def hit_paddle(self, pos):
    paddle_pos = self.canvas.coords(self.paddle.id)
    if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
      if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
        return True
    return False
  
  def draw(self):
    self.canvas.move(self.id, self.x, self.y)

    # current position: [top-left-x, top-left-y, bottom-right-x, bottom-right-y]
    pos = self.canvas.coords(self.id) # current position

    if pos[1] <= 0:                   # Top reached
      self.y = 3
    if pos[3] >= self.canvas_height:
      self.hit_bottom = True
            
    if self.hit_paddle(pos) == True:
      self.y = -3
    if pos[0] <= 0:                   # Left reached
      self.x = 3
    if pos[2] >= self.canvas_width:   # Rightreached
      self.x = -3

class Paddle:
  def __init__(self, canvas, color):
    self.canvas = canvas
    self.id     = canvas.create_rectangle(0, 0, 100, 10, fill=color)

    self.canvas.move(self.id, 200, 300)

    self.x = 0
    self.canvas_width = self.canvas.winfo_width()

    self.canvas.bind_all('<KeyPress-Left>',  self.turn_left)
    self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

  def draw(self):
    self.canvas.move(self.id, self.x, 0)
    
    pos = self.canvas.coords(self.id)
    if pos[0] <= 0:
      self.x = 0
    elif pos[2] >= self.canvas_width:
      self.x = 0

  def turn_left(self, evt):
    self.x = -2
  def turn_right(self, evt):
    self.x = 2

def restart_game():
  """
    Ref:  https://www.daniweb.com/programming/software-development/code/260268/restart-your-python-program
    Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function.
  """
  python = sys.executable
  os.execl(python, python, * sys.argv)
# 2-
def stop_game():
  tk.destroy()


tk = Tk()
tk.title("Game")
tk.resizable(0, 0)                # Set fixed size Window
tk.wm_attributes("-topmost", 1)   # Place Window over all other windows

canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()

btn_restart = Button(tk, text = 'restart', command = restart_game).pack()
btn_stop    = Button(tk, text = 'stop',    command = stop_game).pack() #2-2

tk.update()   # Initializes itself for the game animation

paddle = Paddle(canvas, 'blue')
ball   = Ball(canvas, paddle, 'red')
game_over_text = canvas.create_text(250, 200, text='GAME OVER', state='hidden')

# Main loop:  redraws screen
time.sleep(2)
while(True):
  if ball.hit_bottom == False:
    ball.draw()
    paddle.draw()
  else:
    time.sleep(1)
    canvas.itemconfig(game_over_text, state='normal')

  ball.draw()
  paddle.draw()
  tk.update_idletasks()
  tk.update()
  time.sleep(0.01)

tk.mainloop()