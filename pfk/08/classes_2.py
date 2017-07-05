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
    pass
  def move(self):
    pass
  def eat_food(self):
    pass

class Mammals(Animals):
  def feed_young_with_milk(self):
    pass

class Giraffes(Mammals):
  def eat_leaves_from_trees(self):
    pass

reginald = Giraffes()
reginald.move()
reginald.eat_leaves_from_trees()


