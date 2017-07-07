#!/usr/bin/env python3
################################################################################
#   functions.py
#
#   Python for Kids, Ch. 6: Functions
#
#   05.07.2017  Created by:  zhenya
################################################################################

# Functions are chunks of code that tell Python to do something
# A function has three parts: a name, parameters, and a body

def show_name(name):
  print("hello %s" % name)
  
show_name('Rada')

def full_name(first_name, last_name):
  print("hello %s %s" % (first_name, last_name))
  
#full_name('Rada')              # error: one parameter
full_name('Rada', 'Telyukova')

fname = 'Zhenya'
lname = 'Telyukov'
full_name(fname, lname)

#print(sum(10, 20))             # error: call function before its definition
def sum(var1, var2):
  return var1 + var2

print(sum(10, 20))

# Namespace (Scope of variables)
#print(var1)                    # NameError: name 'var1' is not defined

var1 = 100
print('\nvar1 out of sum1 scope = %i' % var1)
def sum1(var1, var2):
  print('Function Scope: var1 in sum1 = %i' % var1)
  return var1 + var2

print(sum1(10, 20))
print('\nagain: var1 out of sum1 scope = %i' % var1)
