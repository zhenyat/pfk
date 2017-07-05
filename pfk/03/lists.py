#!/usr/bin/env python3
################################################################################
#   lists.py
#
#   Python for Kids, Ch. 3: Lists
#
#   See methods:  https://www.tutorialspoint.com/python/python_lists.htm
#
#   04.06.2017  Created by:  zhenya
################################################################################

nums = [3, 45, -15, 200, 300]
print(nums)
print(nums[1])
print(nums[1:3])  # i=3 not included
print(nums[-2])

greetings = ['Hello', 'привет', 'Hi', 'Morning']
print('\n')
print(greetings)

mix = nums + greetings
print('\n')
print(mix)
print(mix[3:6])

new = [nums, greetings]
print('\n')
print(new)
print(new[0])
print(new[0][2])
print(new[1][1])

# Concatenation
nums = nums + [101, 102, 103]
print('\n')
print(nums)

# Adding Items to a List
nums.append(22)
print('\n')
print(nums)

more_nums = [33, 34, 35]
nums.append(more_nums)
print('\n')
print(nums)

# Removing Items from a List
del nums[2]
print('\n')
print(nums)

# List Arithmetic
list1 = [1,2,3]
list2 = ['Rada', 'Zhenya']
list3 = list1 + list2       # addition
print('\n', list3)
print(list2*3)              # multiplication