#!/usr/bin/env python3

with open('input_files/5.txt') as f:
    instructions = [int(n) for n in f.read().splitlines()]


position = 0
steps = 0

while position < len(instructions):
    new_position = position + instructions[position]
    
    if instructions[position] >= 3:
        instructions[position] -= 1
    else:
        instructions[position] += 1

    position = new_position
    steps += 1

print(steps)
