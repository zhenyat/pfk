#!/usr/bin/env python3
################################################################################
#   time_module.py
#
#   Python for Kids, Ch. 9: module 'time'
#
#   05.07.2017  Created by:  zhenya
################################################################################

import time

print(time.time())

def lots_of_numbers(max):
  t1 = time.time()
  for x in range(0, max):
    print(x)
  t2 = time.time()
  print('it took %s seconds' % (t2-t1))
  
lots_of_numbers(1000)

print(time.asctime())   # current date and time
print(time.localtime())

t = time.localtime()
print('\nYear: %i' % t[0])

t = (2007, 8, 25, 20, 30, 0, 0, 0, 0)
print(time.asctime(t))

for x in range(0, 5):
  print(x)
  time.sleep(1)