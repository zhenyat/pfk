#!/usr/bin/env python3
################################################################################
#   dictionaries.py
#
#   Python for Kids, Ch. 3: Maps / Dictionaries
#
#   16.06.2017  Created by:  zhenya
#   08.07.2019  Last update
################################################################################

# Map is a collection of things == Dictionary

currency = {'Russia': 'Ruble', 'USA': 'USD', 'France': 'Euro'}
print(currency)
print(currency["USA"])

print(currency.keys())
print(currency.values())

keys = currency.keys()
print(type(keys))

values = currency.values()
print(type(values))

for key in keys:
    print(key + ': ' + currency[key])

# TypeError: 'dict_keys' object is not subscriptable
#print(keys[1])