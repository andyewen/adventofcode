import itertools

with open('input.txt') as f:
    numbers = [
        int(line.strip()) for line in f
    ]

for a, b in itertools.combinations(numbers, 2):
    if a + b == 2020:
        print(a * b)
        break
