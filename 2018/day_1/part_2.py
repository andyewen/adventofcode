#!/usr/bin/env python3

with open('input.txt') as fp:
    nums = [int(i) for i in fp.read().splitlines()]

freq = 0
seen = {freq}
done = False

while not done:
    for i in nums:
        freq += i
        if freq in seen:
            print(f'{freq} was seen twice!')
            done = True
            break
        else:
            seen.add(freq)
