#!/usr/bin/env python3
################################################################################
#   modules.py
#
#   Python for Kids, Ch. 7: Modules
#
#   05.07.2017  Created by:  zhenya
################################################################################

# Modules are used to group functions, variables, and other things together 
# into larger, more powerful programs
#
# Built-in Modules:  time, turtle, mcpi, sys ...

import time
print(time.time())  # UNIX Epoch Time: since January 1st, 1970
print(time.ctime()) # current time

# Import as
import time as t

print("\nimport as")
print(t.ctime())

# Import *
from time import *
print("\nimport asterisk")
print(ctime())

# Import from
from time import sleep
print("\nimport from")
print("before sleep...")
sleep(3)
print("...after sleep")
