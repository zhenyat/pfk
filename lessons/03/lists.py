#!/usr/bin/env python3
################################################################################
#   lists.py
#
#   Python for Kids, Ch. 3: Lists
#
#   See methods:  https://www.tutorialspoint.com/python/python_lists.htm
#
#   04.06.2017  Created by:  zhenya
#   08.07.2019  Last update
################################################################################

nums = [3, 45, -15, 200, 300]
print('\nnums:')
print(nums)
print(nums[1])
print(nums[1:3])  # i=3 not included
print(nums[-2])

greetings = ['Hello', 'привет', 'Hi', 'Morning']
print('\ngreetings:')
print(greetings)

mix = nums + greetings
print('\nmix = nums + greetings')
print(mix)
print(mix[3:6])

new = [nums, greetings]
print('\nArray of Arrays: new = [nums, greetings]')
print(new)
print(new[0])
print(new[0][2])
print(new[1][1])

# Concatenation
nums = nums + [101, 102, 103]
print('\nConcatenation: nums = nums + [101, 102, 103]')
print(nums)

# Changing Item
print('\nChanging Item: nums[1]=333')
nums[1] = 444
print(nums)

# Adding Items to a List
nums.append(22)
print('\nAdding Items to a List: nums.append(22)')
print(nums)

# Adding an array as Item
more_nums = [33, 34, 35]
nums.append(more_nums)
print('\nAppend array; nums.append(more_nums)')
print(nums)
print(nums[-1])

# Removing Items from a List
del nums[2]
print('\nRemoving Items from a List: del nums[2]')
print(nums)

# List Arithmetic
list1 = [1,2,3]
list2 = ['Rada', 'Zhenya']
list3 = list1 + list2       # addition
print('\nAddition: ', list3)
print('Multiplication: ', list2*3)