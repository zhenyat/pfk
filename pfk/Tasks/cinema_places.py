#!/usr/bin/env python3
################################################################################
#   cinema_places.py
#
#   Displays free places (additional task to Chapter 3)
#
#   05.06.2017  Created by:  zhenya
#   05.07.2017  try except
#   06.07.2017  comments to __future__
################################################################################
from __future__ import print_function  # must be 1st line (NB bug for separators 'end'?)
import sys

ROWS = 5
COLS = 10

def show_free(places):
  print("Free seats:")
  for i in range(0, ROWS):
    print("\nRow %d:" % (i+1), end='')
    for j in range(0, COLS):
      if (places[i][j] == 1):
        print("%3d" % (j+1), end='')
      else:
        print("   ", end='')
  print('\n')

# places = [[1]*10, [1]*10, [1]*10, [1]*10, [1]*10]

places = []
for i in range(ROWS):
  places.append([1]*COLS)

show_free(places)   # all seats are available

# input result: '2 5'
# split result: ['2', '5']
# map result: row = 2, col = 5

while(True):
  answer = input("Enter 2 values 'row seat' or press Enter to stop: ").split()
  if (len(answer) == 0):
    sys.exit("Job completed")
  elif (len(answer) != 2):
    print("Must be 2 values: row seat")
  else:
    try:
      row, col = map(int, answer)
  
      if ((row < 1 or row > ROWS) or (col < 1 or col > COLS)):
        print("No such seat")
      else:
        if (places[row-1][col-1] == 0):
          print("This seat is busy")
        else:
          places[row-1][col-1] = 0
          show_free(places) 
    except Exception:
      sys.exit("Something wrong! Job completed")
