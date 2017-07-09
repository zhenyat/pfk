#!/usr/bin/env python3
################################################################################
#   pickle_module.py
#
#   Python for Kids, Ch. 9: module 'pickle'
#
#   05.07.2017  Created by:  zhenya
################################################################################

import pickle

game_data = {
  'player-position' : 'N23 E45',
  'pockets'         : ['keys', 'pocket knife', 'polished stone'],
  'backpack'        : ['rope', 'hammer', 'apple'],
  'money'           : 158.50
}

fout = open('game_data.dat', 'wb')
pickle.dump(game_data, fout)
print('Data saved')
fout.close()

fin         = open('game_data.dat', 'rb')
loaded_data = pickle.load(fin)
print('Loaded data:')
print(loaded_data)