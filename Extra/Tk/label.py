#!/usr/bin/env python3
################################################################################
#   label.py
#
#   https://www.youtube.com/watch?v=yqo_PcecZXQ
#
#   16.03.2018  Created by:  zhenya
################################################################################

from tkinter import *

my_window = Tk()
my_window.title("Greeting")
my_window.configure(background='yellow')

Label(my_window, text = 'Hello World!', bg='lightyellow', fg = 'blue', font = 'none, 16 italic bold').pack()
my_window.geometry("300x200+300+500")

my_window.mainloop()