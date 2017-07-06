#!/usr/bin/env python3
################################################################################
#   6_text.py
#
#   Python for Kids, Ch. 12: Tkinter text
#
#   06.07.2017  Created by:  zhenya
################################################################################


from tkinter import *

tk     = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()

canvas.create_text(150, 100, text='There once was a man from Toulouse,')

canvas.create_text(150, 150, text='He said, "It\'s my curse,', font=('Times', 15))
canvas.create_text(200, 200, text='But it could be worse,',    font=('Helvetica', 20))
canvas.create_text(220, 250, text='My cousin rides round',     font=('Courier', 22))
canvas.create_text(220, 300, text='on a goose."',              font=('Courier', 30))

tk.mainloop()