#!/usr/bin/env python3
import re

filename = 'input_files/2.txt'

with open(filename, 'r') as file:
    inputlines = file.readlines()

numpad = (('', '', '1', '', ''),
          ('', '2', '3', '4', ''),
          ('5', '6', '7', '8', '9'),
          ('', 'A', 'B', 'C', ''),
          ('', '', 'D', '', ''))

currentbutton = [0, 2]
combination = ''

for line in inputlines:
    for command in line:
        newbutton = currentbutton[:]
        directions = {'U': (0, -1),
                      'D': (0, 1),
                      'L': (-1, 0),
                      'R': (1, 0)}

        direction = directions.get(command)
        if direction:
            newbutton[0] += direction[0]
            newbutton[1] += direction[1]
            newbutton[0] = min(max(newbutton[0], 0), 4)
            newbutton[1] = min(max(newbutton[1], 0), 4)
            if numpad[newbutton[1]][newbutton[0]]:
                currentbutton = newbutton

    combination += numpad[currentbutton[1]][currentbutton[0]]

print(combination)



