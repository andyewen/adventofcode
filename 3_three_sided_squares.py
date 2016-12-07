#!/usr/bin/env python3
import re

filename = 'input_files/3.txt'
with open(filename, 'r') as filename:
    inputlines = filename.readlines()

rexp = re.compile('\s+')
inputlines = [list(map(int, re.split(rexp, line.strip())))
              for line in inputlines]

triangles = []
for r in range(0, len(inputlines), 3):
    for c in range(3):
        triangles.append([inputlines[r][c],
                          inputlines[r + 1][c],
                          inputlines[r + 2][c]])

def validate_triangle(t):
    if t[0] + t[1] <= t[2]:
        return False
    if t[0] + t[2] <= t[1]:
        return False
    if t[1] + t[2] <= t[0]:
        return False
    return True

n_actual_triangles = sum(map(validate_triangle, triangles))
print(n_actual_triangles)
