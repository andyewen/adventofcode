#!/usr/bin/env python3
import itertools

with open('input.txt') as fp:
    lines = fp.read().splitlines()

for a, b in itertools.combinations(lines, 2):
    remove = []
    for c_a, c_b in zip(a, b):
        if c_a != c_b:
            remove.append(c_a)

    if len(remove) == 1:
        answer = a.replace(remove[0], '')
        print(f'Answer is {answer}')
