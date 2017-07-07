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
  def __init__(self, spots):
    self.giraffe_spotes = spots
    
  def eat_leaves_from_trees(self):
    self.eat_food()
    
  def find_food(self):
    self.move()
    print("I've found food!")
    self.eat_food()

  def dance(self):
    print("I'm dancing...")
    for i in range(5):
      self.move()

print('\nBob:')
bob = Giraffes(100)
print('Bob has %i spots' % bob.giraffe_spotes)
bob.move()
bob.eat_leaves_from_trees()

print('\nJohn:')
john = Giraffes(150)
print('John has %i spots' % john.giraffe_spotes)
john.breathe()
john.move()
john.eat_food()

print('\nBob:')
bob.find_food()

print('\nJohn:')
john.dance()

# Error
#new = Giraffes()   # TypeError: __init__() missing 1 required positional argument: 'spots
#print('New has %i spots' % new.giraffe_spotes)