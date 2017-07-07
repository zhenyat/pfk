#!/usr/bin/env python3
################################################################################
#   arcs.py
#
#   Python for Kids, Ch. 12: Tkinter arcs
#
#   Arc is in rectangular (top-left-x, top-left-y, bottom-right-x. bottom-right-y)
#
#   canvas.create_arc(top-left-x, top-left-y, bottom-right-x. bottom-right-y,
#                     extent=<angle>, style=ARC)
#
#   06.07.2017  Created by:  zhenya
################################################################################

from tkinter import *

tk     = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()

canvas.create_arc(10, 10, 200, 80, extent=45, style=ARC)    # counterclock
canvas.create_arc(10, 80, 200, 160, extent=90, style=ARC)
canvas.create_arc(10, 160, 200, 240, extent=135, style=ARC)
canvas.create_arc(10, 240, 200, 320, extent=180, style=ARC)
canvas.create_arc(10, 320, 200, 400, extent=359, style=ARC)  # NOT 360

tk.mainloop()