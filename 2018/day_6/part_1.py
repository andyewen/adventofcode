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

closest_stats = Counter()
for y in range(min_y, max_y + 1):
    for x in range(min_x, max_x + 1):
        distances = [manhattan_distance(point_coord, (x, y)) for point_coord in coords]
        distances = sorted(enumerate(distances), key=lambda t: t[1])
        if distances[0][1] != distances[1][1]:
            closest_stats[distances[0][0]] += 1
        if x == min_x or x == max_x or y == min_y or y == max_y:
            coord_is_infinite[distances[0][0]] = True

closest_stats = {k: v for k, v in closest_stats.items() if not coord_is_infinite[k]}
print(sorted(closest_stats.values()))
