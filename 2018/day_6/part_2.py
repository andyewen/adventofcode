#!/usr/bin/env python3
from collections import Counter
import re

line_regex = re.compile(r'(\d+),\s+(\d+)')


def parse_line(l):
    m = line_regex.match(l)
    return (int(m.group(1)), int(m.group(2)))


def manhattan_distance(p1, p2):
    return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])


with open('input.txt') as fp:
    coords = [parse_line(line) for line in fp]
coord_is_infinite = [False] * len(coords)

min_x = min(c[0] for c in coords)
max_x = max(c[0] for c in coords)
min_y = min(c[1] for c in coords)
max_y = max(c[1] for c in coords)

squares_in_area_count = 0
for y in range(min_y, max_y + 1):
    for x in range(min_x, max_x + 1):
        summed_distances = sum(manhattan_distance(point_coord, (x, y)) for point_coord in coords)
        if summed_distances < 10000:
            squares_in_area_count += 1

print(squares_in_area_count)
