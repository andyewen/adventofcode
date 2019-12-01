#!/usr/bin/env python3
def calculate_fuel(mass):
    fuel = mass // 3 - 2
    if fuel <= 0:
        return 0
    return fuel + calculate_fuel(fuel)


with open('input.txt') as f:
    lines = f.read().splitlines()

total_fuel = sum(
    calculate_fuel(int(line)) for line in lines
)

print(f'Total fuel is: {total_fuel}')
