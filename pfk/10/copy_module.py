#!/usr/bin/env python3
################################################################################
#   modules.py
#
#   Python for Kids, Ch. 9: module 'copy'
#
#   05.07.2017  Created by:  zhenya
################################################################################

# A Python module is any combination of functions, classes, and variables.
# Python uses modules to group functions and classes in order to make them easier to use

import copy

class Animal:
  def __init__(self, species, number_of_legs, color):
    self.species        = species
    self.number_of_legs = number_of_legs
    self.color          = color
    
print('\n copy() of animal')

harry   = Animal('hippogriff', 6, 'pink')
harriet = copy.copy(harry)
print(harry.species)
print(harriet.species)

print('\n copy() of List of animals')

harry = Animal('hippogriff', 6, 'pink')
carrie = Animal('chimera', 4, 'green polka dots')
billy  = Animal('bogill', 0, 'paisley')

my_animals   = [harry, carrie, billy]
more_animals = copy.copy(my_animals)

# The same objects id
print(my_animals)     # List of objects id
print(more_animals)   # List of objects id

print(more_animals[0].species)
print(more_animals[1].species)

my_animals[0].species = 'ghoul'
print(my_animals[0].species)
print(more_animals[0].species)

sally = Animal('sphinx', 4, 'sand')
my_animals.append(sally)
print(len(my_animals))
print(len(more_animals))

print('\n deepcopy() of List of animals')

more_animals          = copy.deepcopy(my_animals)
my_animals[0].species = 'wyrm'

print(my_animals[0].species)
print(more_animals[0].species)

# Different objects id
print(my_animals)
print(more_animals)  # List of objects id
