#!/usr/bin/env python3
################################################################################
#   sys_module.py
#
#   Python for Kids, Ch. 9: module 'sys'
#
#   05.07.2017  Created by:  zhenya
################################################################################

import sys

print('\n stdin')
print("enter text line:")
v = sys.stdin.readline()
print(v)

print("enter new text line:")
v = sys.stdin.readline(10)
print(v)

print('\n stdin')
sys.stdout.write("What does a fish say when it swims into a wall? Dam.")

print('\n Python version')
print(sys.version)

sys.exit('end')