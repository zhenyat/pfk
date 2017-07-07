#!/usr/bin/env python3
################################################################################
#   5_polygons.py
#
#   Python for Kids, Ch. 12: Tkinter polygons
#
#   06.07.2017  Created by:  zhenya
################################################################################

from tkinter import *

tk     = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()

canvas.create_polygon(10, 10, 100, 10, 100, 110, fill="", outline="red")    # triangle
canvas.create_polygon(200, 10, 240, 30, 120, 100, 140, 120, fill="", outline="blue")

tk.mainloop()