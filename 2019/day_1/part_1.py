#!/usr/bin/env python3
with open('input.txt') as f:
    file_contents = f.read()

lines = file_contents.splitlines()

total_fuel = 0
for line in lines:
    module_mass = int(line)
    module_fuel = module_mass // 3 - 2
    total_fuel += module_fuel

print(f'Total fuel is: {total_fuel}')
