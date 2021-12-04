range = 0
depth = 0

with open('input.txt') as f:
    for line in f:
        line = line.rstrip('\n')
        direction, distance = line.split()
        distance = int(distance)

        if direction == 'forward':
            range += distance
        elif direction == 'up':
            depth -= distance
        elif direction == 'down':
            depth += distance


print(f'{range=}, {depth=}')
print(f'{range * depth=}')
