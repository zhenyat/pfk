#!/usr/bin/env python3
################################################################################
#   classes.py
#
#   Python for Kids, Ch. 8: Classes
#
#   05.07.2017  Created by:  zhenya
################################################################################

class Things:
  pass

class Inanimate(Things):
  pass

class Sidewalks(Inanimate):
  pass

class Animate(Things):
  pass

class Animals(Animate):
  def breathe(self):
    print('breathing')
  def move(self):
    print('moving')
  def eat_food(self):
    print('eating food')

class Mammals(Animals):
  def feed_young_with_milk(self):
    print('feeding young')

class Giraffes(Mammals):
  def eat_leaves_from_trees(self):
    print('eating leaves')

print('\nBob:')
bob = Giraffes()
bob.move()
bob.eat_leaves_from_trees()

print('\nJohn:')
John = Giraffes()
John.breathe()
John.move()
John.eat_food()
