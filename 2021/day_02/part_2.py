range = 0
depth = 0
aim = 0

with open('input.txt') as f:
    for line in f:
        line = line.rstrip('\n')
        direction, amount = line.split()
        amount = int(amount)

        if direction == 'forward':
            range += amount
            depth += aim * amount
        elif direction == 'up':
            aim -= amount
        elif direction == 'down':
            aim += amount

print(f'{range=}, {depth=}')
print(f'{range * depth=}')
