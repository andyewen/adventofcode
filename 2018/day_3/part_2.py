#!/usr/bin/env python3
import re
from collections import defaultdict

square_re = r'#(?P<id>\d+)\s+@\s+(?P<x>\d+),(?P<y>\d+):\s+(?P<w>\d+)x(?P<h>\d+)'
square_re = re.compile(square_re)


def process_line(l):
    square = square_re.match(l).groupdict()
    for k in square:
        square[k] = int(square[k])
    return square


with open('input.txt') as fp:
    squares = [process_line(line) for line in fp]

rectangle = defaultdict(list)
for square in squares:
    for j in range(square['y'], square['y'] + square['h']):
        for i in range(square['x'], square['x'] + square['w']):
            rectangle[(i, j)].append(square['id'])

for square in squares:
    is_overlapping = False
    for j in range(square['y'], square['y'] + square['h']):
        for i in range(square['x'], square['x'] + square['w']):
            if len(rectangle[(i, j)]) > 1:
                is_overlapping = True
                break
        if is_overlapping:
            break

    if not is_overlapping:
        print(f'Square #{square["id"]} does not overlap')
        break
else:
    print('Could not find a non-overlapping square.')
