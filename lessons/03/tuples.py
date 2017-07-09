#!/usr/bin/env python3
################################################################################
#   tuples.py
#
#   Python for Kids, Ch. 3: Tuples
#
#   16.06.2017  Created by:  zhenya
#   05.07.2017  Last update
################################################################################

holidays = ('January, 1st', 'February, 23rd', 'March, 8th', 'May, 1st', 
            'June, 12th',   'November, 4th')

print(holidays)
print(holidays[2])

days_of_week = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
print(days_of_week)

# Error:  "TypeError: 'tuple' object does not support item assignment"
holidays[1] = 'blah'