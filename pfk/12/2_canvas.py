#!/usr/bin/env python3
################################################################################
#   canvas.py
#
#   Python for Kids, Ch. 12: Tkinter canvas
#
#   05.07.2017  Created by:  zhenya
################################################################################

from tkinter import *

tk   = Tk()
cnvs = Canvas(tk, width=500, height=500)
cnvs.pack()
cnvs.create_line(0, 0, 500, 500)
cnvs.create_rectangle(100, 100, 200, 400)


tk.mainloop()