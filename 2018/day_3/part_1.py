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

total = sum((len(square_inch) > 1) for square_inch in rectangle.values())
print(f'Answer is: {total}')
