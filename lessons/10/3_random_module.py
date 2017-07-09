#!/usr/bin/env python3
################################################################################
#   random_module.py
#
#   Python for Kids, Ch. 9: module 'random'
#
#   05.07.2017  Created by:  zhenya
################################################################################

import random

print('\n Random values')
print(random.randint(1, 100))
print(random.randint(100, 1000))
print(random.randint(1000, 5000))

print('\n Random item from a List')
desserts = ['ice cream', 'pancakes', 'pie', 'cookies', 'candy']
print(random.choice(desserts))

random.shuffle(desserts)
print(desserts)