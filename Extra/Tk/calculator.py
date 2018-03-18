#!/usr/bin/env python3
################################################################################
#   calculator.py
#
#   https://www.youtube.com/watch?v=ieW0ccjpNyc
#
#   17.03.2018  Created by:  zhenya
################################################################################

from tkinter import *
from functools import partial

number   = 1
ops_keys = ("+", "-", "*", "/")
row      = 0

main = Tk()
main.title("My Calculator")
main.geometry("500x500+300+300")

### Functions
def do_calc(data):
  in_box.insert(END, str(data))

def calculate():
  try:
    sum    = in_box.get()
    result = eval(sum)
    out_box.insert(END, str(result) + "\n")
  except SyntaxError:
    out_box.insert(END, "Invalid input\n")
    
### Widgets

# Frames / Labels
Label(main, text='Calculator', font = 16).grid(row = 0, column = 0, sticky = W)

numpad = Frame()
numpad.grid(row = 2, column = 0, sticky = W)

operations = Frame()
operations.grid(row = 2, column = 1)

# Entry Boxes
in_box = Entry(main, width = 35, bg = 'light grey')
in_box.grid(row = 1, column = 0)

# Text Boxes
out_box = Text(main, width = 50, heigh =5 , wrap = WORD, bg = 'light yellow')
out_box.grid(row = 4, column = 0, sticky = W)

# Buttons
for row in range(3):
  for column in range(3):
    Button(numpad, text=number, width = 10, command = partial(do_calc, number)).grid(row = row, column = column, sticky = W)
    number += 1

#row = 0
for key in ops_keys:
  Button(operations, text = key, width =  10, command = partial(do_calc, key)).grid(row = row, column = 0, sticky = W)
  row += 1

Button(main, text = '=', width = 10, command = calculate).grid(row = 3, column = 0, sticky = W)

######################
main.mainloop()