#!/usr/bin/env python3
filename = 'input_files/1.txt'
with open(filename, 'r') as inputfile:
    input_string = inputfile.read()

commands = input_string.split(', ')

visited_locations = {(0, 0)}
x, y = 0, 0
direction = 0

def travel(distance, cardinal):
    global x, y, visited_locations
    dx, dy = 0, 0

    if cardinal == 0:
        dy = 1
    elif cardinal == 1:
        dx = 1
    elif cardinal == 2:
        dy = -1
    else:
        dx = -1

    for _ in range(distance):
        if dx:
            x += dx
        else:
            y += dy

        if (x, y) in visited_locations:
            return True
        visited_locations.add((x, y))

    return False

for command in commands:
    if command[0] == 'L':
        direction -= 1
    else:
        direction += 1

    distance = int(command[1:])
    cardinal = direction % 4
    revisited = travel(distance, cardinal)

    if revisited:
        break

print('Distance from 0, 0 to {}, {} is: {}.'.format(x, y, x + y))

