#!/usr/bin/env python3
################################################################################
#   6_sample.py
#
#   Tk_Canvas_ticker1.py
#   using a Tkinter canvas to create a marquee/ticker via
#   canvas.create_text(x, y, anchor='nw', text=s, font=font)
#   canvas.move(object, x_increment, y_increment)
#   tested with Python27 and Python33  by  vegaseat  04oct2013#
#
#   https://www.daniweb.com/programming/software-development/code/464630/a-ticker-for-long-messages-python-tkinter
#
#   12.03.2018  Created by:  zhenya
################################################################################
import time
try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk
    
root = tk.Tk()

canvas = tk.Canvas(root, height=80, width=600, bg="yellow")
canvas.pack()

font       = ('courier', 48, 'bold')
text_width = 15

s1 = "We don't really care why the chicken crossed the road.  "
s2 = "We just want to know if the chicken is on our side of the "
s3 = "road or not. The chicken is either for us or against us.  "
s4 = "There is no middle ground here.  (George W. Bush)"

s5 = ' ' * text_width             # pad front and end of text with spaces
s = s5 + s1 + s2 + s3 + s4 + s5   # concatenate it all
x = 1
y = 2

text = canvas.create_text(x, y, anchor='nw', text=s, font=font)
dx   = 1
dy   = 0  # use horizontal movement only

# the pixel value depends on dx, font and length of text
pixels = 9000
for p in range(pixels):
    # move text object by increments dx, dy
    # -dx --> right to left
    canvas.move(text, -dx, dy)
    canvas.update()
    
    time.sleep(0.005)           # shorter delay --> faster movement
    #print(k)                   # test, helps with pixel value

root.mainloop()