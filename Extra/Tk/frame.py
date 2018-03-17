#!/usr/bin/env python3
################################################################################
#   frame.py
#
#   https://www.youtube.com/watch?v=qYXMLFrcYCI
#
#   17.03.2018  Created by:  zhenya
################################################################################

from tkinter import *

def speak():
  pass

main = Tk()
main.title('My GUI')
main.geometry("400x400")

my_frame = Frame(main)
my_frame.grid(row = 1, column = 0, sticky = W)

Label(main, text = 'This is my GUI').grid(row = 0, column = 0, sticky = W)

Button(my_frame, text = 'One', width = 12, command = speak).grid(row = 0, column = 0, sticky = W)
Button(my_frame, text = 'Two', width = 12, command = speak).grid(row = 0, column = 1, sticky = W)

main.mainloop()