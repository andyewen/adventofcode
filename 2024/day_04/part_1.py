grid = []
with open('input.txt') as in_file:
    for line in in_file:
        line = line.strip()
        grid.append(list(line))

directions = [
    (1, 0),
    (1, 1),
    (0, 1),
    (-1, 1),
    (-1, 0),
    (-1, -1),
    (0, -1),
    (1, -1),
]

x = 1
y = 1
for (a, b) in directions:
    print(grid[y + b][x + a])
