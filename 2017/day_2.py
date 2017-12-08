#!/usr/bin/env python3
from itertools import permutations

with open('input_files/2.txt') as f:
    lines = list(f)

sum = 0
for l in lines:
    for (x, y) in permutations((int(n) for n in l.split()), 2):
        if x % y == 0:
            sum += x // y
            break

print(sum)
