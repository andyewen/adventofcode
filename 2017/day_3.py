#!/usr/bin/env python3
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
with_diagonals = directions + [(1, 1), (1, -1), (-1, -1), (-1, 1)]
d = 0
position = (0, 0)
address = 265149

grid = {}


def add(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])


def sum_neighbours(grid, position):
    neighbours = (add(position, d) for d in with_diagonals)

    total = 0
    for n in neighbours:
        value = grid.get(n)
        if value is not None:
            total += value
    return total


while True:
    grid[position] = sum_neighbours(grid, position) or 1
    print(grid[position])
    if grid[position] > 265149:
        break

    position = add(position, directions[d])

    turned = (d + 1) % len(directions)
    if (add(position, directions[turned]) not in grid):
        d = turned
