#!/usr/bin/env python3
################################################################################
#   button.py
#
#   https://www.youtube.com/watch?v=vAca_IfSNDw
#
#   17.03.2018  Created by:  zhenya
################################################################################

from tkinter import *

# Make variables
counter = 0

# Functions
def add():
  global counter
  counter += 1
  lbl_res.config(text = counter)
  
def substract():
  global counter
  counter -= 1
  lbl_res.config(text = counter)
  
main_window = Tk()

# Widgets and stuff
lbl_res = Label(main_window, text = 'zero')
btn_add =Button(main_window, text = 'Add Count', command = add)
btn_sub =Button(main_window, text = 'Substract Count', command = substract)

lbl_res.pack()
btn_add.pack(side = LEFT)
btn_sub.pack(side = LEFT)

main_window.geometry("300x200+250+250")

main_window.mainloop()

