################################################################################
#   loops.py
#
#   Python for Kids, Ch. 6: Loops
#
#   05.07.2017  Created by: zhenya
#   08.07.2019  Last update
################################################################################

### FOR Loop
for i in range(0, 5):
  print('%s: hello' % i)
  
print('\n')
for i in range(5):
  print('again %s: hello' % i)

print('\n')
print(list(range(10, 20)))

# Iteration (repetition)
games_list = ['Minecraft', 'World of Tanks']
print('\nMy games:')
for game in games_list: print(game)

days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
print('\nDays of Week:')
for day in days: print(day)


### WHILE Loop
print('\nWHILE Loop:')
step = 0
while step < 10:
  print(step)
  step = step + 1

print('\nWHILE True Loop:')
step = 0
while True:
    print(step)
    step += 1
    if (step == 5): break