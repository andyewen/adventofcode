#!/usr/bin/env python3
input_string = 'L4, L1, R4, R1, R1, L3, R5, L5, L2, L3, R2, R1, L4, R5, R4, L2, R1, R3, L5, R1, L3, L2, R5, L4, L5, R1, R2, L1, R5, L3, R2, R2, L1, R5, R2, L1, L1, R2, L1, R1, L2, L2, R4, R3, R2, L3, L188, L3, R2, R54, R1, R1, L2, L4, L3, L2, R3, L1, L1, R3, R5, L1, R5, L1, L1, R2, R4, R4, L5, L4, L1, R2, R4, R5, L2, L3, R5, L5, R1, R5, L2, R4, L2, L1, R4, R3, R4, L4, R3, L4, R78, R2, L3, R188, R2, R3, L2, R2, R3, R1, R5, R1, L1, L1, R4, R2, R1, R5, L1, R4, L4, R2, R5, L2, L5, R4, L3, L2, R1, R1, L5, L4, R1, L5, L1, L5, L1, L4, L3, L5, R4, R5, R2, L5, R5, R5, R4, R2, L1, L2, R3, R5, R5, R5, L2, L1, R4, R3, R1, L4, L2, L3, R2, L3, L5, L2, L2, L1, L2, R5, L2, L2, L3, L1, R1, L4, R2, L4, R3, R5, R3, R4, R1, R5, L3, L5, L5, L3, L2, L1, R3, L4, R3, R2, L1, R3, R1, L2, R4, L3, L3, L3, L1, L2'

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

