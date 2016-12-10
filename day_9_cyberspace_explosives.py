#!/usr/bin/env python3
import re

filename = 'input_files/9.txt'
with open(filename) as inputfile:
    inputstring = inputfile.read()

    
def replace(m):
    num_characters = int(m.groups()[0])
    repeat_count = int(m.groups()[1])
    return m.string[m.end():m.end() + num_characters] * repeat_count

marker_pattern = r'\((\d+)x(\d+)\)'
print(len(re.sub(marker_pattern, replace, inputstring)))
