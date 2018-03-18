#!/usr/bin/env python3
################################################################################
#   front_end.py
#
#   TBD: https://www.youtube.com/watch?v=ddoPYppcppc
#
#   18.03.2018  Created by:  zhenya
################################################################################

from tkinter import *

main = Tk()
main.title('Dummy')
main.geometry("300x300+300+300")

### Functions
def dummy():
  text = input_box.get()
  output_box.insert(END, text)
  input_box.delete(0, END)

### Widgets

# Frames / Labels
label_dummy  = Label(main, text = 'Dummy Label')

# Entry Boxes
input_box = Entry(main, width = 20, bg = 'light grey')

# Text Boxes
output_box = Text(main, width = 20, heigh = 5, bg = 'light yellow')

# Buttons
button_dummy = Button(main, text = 'Dummy Button', command = dummy)

### Grids
label_dummy.grid( row = 0, column = 0, sticky = W)
input_box.grid(   row = 1, column = 0, sticky = W)
button_dummy.grid(row = 2, column = 0, sticky = W)
output_box.grid(  row = 3, column = 0, sticky = W)

### Packs
#label_dummy.pack()
#button_dummy.pack(side = LEFT)
#input_box.pack(side = LEFT)
#output_box.pack()


######################
main.mainloop()