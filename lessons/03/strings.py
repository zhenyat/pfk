#!/usr/bin/env python3
################################################################################
#   strings.py
#
#   Python for Kids, Ch. 3: Strings
#
#   04.06.2017  Created by:  zhenya
################################################################################

# Single string
question = "How are you?"
print(question)
print('\n')
three_single_quote_str = '''He said, "Aren't can't shouldn't wouldn't."'''
print(three_single_quote_str)

# Escaping
single_quote_str = 'He said, "Aren\'t can\'t shouldn\'t wouldn\'t."'
print(single_quote_str)

double_quote_str = "He said, \"Aren't can't shouldn't wouldn't.\""
print(double_quote_str)

# Multiple strings
print('\n')
text = '''This is a text with
          multiple lines.
this is the last line'''
print(text)

# Embedding Values in Strings
print('\n')
age = 9
print('I am %s years old' % age)

name = 'Rada'
print('My name is %s. I am %s years old' % (name, age))

# Multiplying Strings
print('\n')
print('2'*5, ' '*10, 'stop'*2)

for i in range(0, 10):
  print(' '*i + '\\')
for i in range(9, -1, -1):
  print(' '*i + '/')

print('end')