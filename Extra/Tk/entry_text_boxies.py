#!/usr/bin/env python3
################################################################################
#   entry_text_boxies.py
#
#   https://www.youtube.com/watch?v=ieW0ccjpNyc
#
#   17.03.2018  Created by:  zhenya
################################################################################
from tkinter import *

main = Tk()
main.title('Input Output')
main.geometry("300x300+300+300")

# Functions
def copy():
  text = input_box.get()
  output_box.insert(END, text)
  input_box.delete(0, END)
  
input_box = Entry(main, width = 20, bg = 'light grey')
input_box.grid(row = 0, column = 0, sticky = W)

Button(main, width = 10, text = 'Copy me', command = copy).grid(row = 1, column = 0, sticky = W)

output_box = Text(main, width = 20, heigh = 5, bg = 'light yellow')
output_box.grid(row = 2, column = 0, sticky = W)

input_box.focus_set()

main.mainloop()