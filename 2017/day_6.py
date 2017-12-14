#!/usr/bin/env python3
with open('input_files/6.txt') as f:
    banks = [int(b) for b in f.read().split()]

seen = set()
duplicate = None
cycles = 0

while True:
    seen.add(tuple(banks))

    max_bank, amount = max(enumerate(banks), key=lambda x: x[1])
    banks[max_bank] = 0
    for i in range(1, amount + 1):
        i = (max_bank + i) % len(banks)
        banks[i] += 1

    banks_tuple = tuple(banks)
    if duplicate is not None:
        # Count cycles until duplicate is seen again.
        cycles += 1
        if banks_tuple == duplicate:
            break
    elif banks_tuple in seen:
        # Found duplicate.
        duplicate = banks_tuple

print(cycles)
