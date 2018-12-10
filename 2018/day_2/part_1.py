#!/usr/bin/env python3
from collections import Counter

with open('input.txt') as fp:
    lines = fp.read().splitlines()

twos = 0
threes = 0

for l in lines:
    c = Counter(l)
    values = set(c.values())
    twos += (2 in values)
    threes += (3 in values)

answer = twos * threes
print(f'Solution is {twos} x {threes} = {answer}')
