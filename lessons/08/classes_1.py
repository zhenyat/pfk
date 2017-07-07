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
  pass

class Mammals(Animals):
  pass

class Giraffes(Mammals):
  pass

reginald = Giraffes()
