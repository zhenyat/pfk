#!/usr/bin/env python3
################################################################################
#   7_images.py
#
#   Python for Kids, Ch. 12: Tkinter images
#
#   NB! PhotoImage is for GIF images ONLY!
#   Use Python Imaging Library for other formats:
#     $ pip3 install Pillow  ==> Pillow-4.2.0 olefile-0.4
#
#   06.07.2017  Created by:  zhenya
################################################################################

from tkinter import *

tk     = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()

# GIF only!!
my_image = PhotoImage(file='./globe.gif')
canvas.create_image(30, 30, anchor=NW, image=my_image)

# Other image formats
from PIL import Image, ImageTk

img = Image.open("zt.jpg")
img.show()

tk.mainloop()

