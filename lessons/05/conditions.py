################################################################################
#   conditions.py
#
#   Python for Kids, Ch. 5: IF statements
#
#   05.07.2017  Created by: zhenya
#   08.07.2019  Last update
################################################################################

answer = input("enter 2 digits: ").split()
a, b = map(int, answer)

if (a == b):
  print("a = b")

if (a != b):
 print("a != b")

if (a < b):
  print("a < b")
elif (a > b):
  print("a > b")
else:
  print('two equal values')
  

age = int(input("age: "))

if age <7:
  print('not a school')
elif age >=7 and age < 11:
  print('primary school')
elif age >= 11 and age < 15:
  print('midle school')
elif age >= 15 and age <=17:
  print('high school')
else:
  print('out of school!')
  
# NONE: no value

x = None
print(x)
if x == None:
  print("No value for x")

# String vs Integer
answer = input("enter 10: ")
print(type(answer))
if answer == 10:      
  print('It is integer 10')
else:
  print('It is not string "10"')

answer = input("enter 10: ")
print(type(answer))
if int(answer) == 10:      
  print('It is integer 10')
else:
  print('It is not string "10"')

if True: print('true')
else:    print('false')