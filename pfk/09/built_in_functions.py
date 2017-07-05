#!/usr/bin/env python3
################################################################################
#   built_in_functions.py
#
#   Python for Kids, Ch. 9: Built-in Functions (12 functions)
#
#   05.07.2017  Created by:  zhenya
################################################################################

# abs()
print('\nabs()')
print(abs(4))
print(abs(-4))
print(abs(0))

# bool()
print('\nbool()')
print(bool(0))
print(bool(None))

print(bool(1))
print(bool(-20))
print(bool(34.5))
print(bool('Rada'))

#dir()
print('\ndir()')
print('\n')
print(dir('s'))
print('\n')
print(dir(1))
name = 'Rada'
print('\n')
print(dir(name))
print('\n')
print(dir(name.upper))

#eval() - evaluate
print('\neval()')
print(eval('2*5'))

#calc = input("enter arithmetic operation: ")
#print(eval(calc))

#exec() - more complicacted programs
print('\nexec()')
my_prog = '''
print('sun')
print('moon')'''
exec(my_prog)

# float()
print('\nfloat()')
print(float(12))
print(float('-123'))
print(float(36.60))

# int()
print('\nint()')
print(int(23.3))
print(int('25'))

# len()
print('\nlen()')
my_str = 'My name is Rada'
print(len(my_str))
my_arr = [1,2,3,4,5]
print(len(my_arr))
my_cur = {'Russia': 'Ruble', 'USA': 'Dollar', 'Germany': 'Euro'}
print(len(my_cur))

# max(), min()
print('\nmax() / min()')
num = [0, 10, -22, 45, 17]
print(max(num))
print(min(num))

string = "This-is-a-string.Wow!"
print(max(string))
print(min(string))

# range()
print('\nrange()')
for i in range(0, 5):
  print(i)
print(list(range(5)))
print(list(range(0, 20, 2)))  # even values

# sum()
print('\nsum()')
print(sum(list(range(0, 20, 2))))

# Files
print('\nFiles')
fin = open('./my_file.txt')
text = fin.read()
print(text)
fin.close()

fout = open('./new_file.txt', 'w')
fout.write(text)
fout.close()

# Error
#fout = open('./test.txt')  # FileNotFoundError: [Errno 2] No such file or directory: './new_file.txt'