#!/usr/bin/env python3
import re
from time import sleep

filename = 'input_files/8.txt'
with open(filename) as inputfile:
    commands = inputfile.read().splitlines()

w, h = 50, 6
screen = [[0] * 50 for i in range(6)]

def rect_command(w, h):
    global screen
    for j in range(h):
        for i in range(w):
            screen[j][i] = 1

def rotate(l, n):
    return l[-n:] + l[:-n]

def rotate_command(dimension, index, amount):
    global screen
    if dimension == 'row':
        screen[index] = rotate(screen[index], amount)
    elif dimension == 'column':
        l = [r[index] for r in screen]
        l = rotate(l, amount)
        for i, r in enumerate(screen):
            r[index] = l[i]

for command in commands:
    t = command.split()[0]
    if t == 'rect':
        m = re.match(r'rect (\d+)x(\d+)', command)
        if m:
            rect_command(int(m.groups()[0]), int(m.groups()[1]))
    elif t == 'rotate':
        m = re.match(r'rotate (\w+) \w=(\d+) by (-?\d+)', command)
        if m:
            rotate_command(m.groups()[0], int(m.groups()[1]), int(m.groups()[2]))

print('{}/{}'.format(sum(p for r in screen for p in r), w * h))
for r in screen:
    print(''.join(map(lambda p: '█' if p else ' ', r)))
