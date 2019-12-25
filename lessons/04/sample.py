#!/usr/bin/env python3
################################################################################
#   sample.py
#
#   Python for Kids, Ch. 4: Turtle
#
#   06.07.2017  Created by:  zhenya
################################################################################
import turtle

main_window = turtle.Screen()  
t  = turtle.Pen()     # or t  = turtle.Turtle()

t.fd(100)
t.lt(90)
t.fd(100)

main_window.mainloop()
