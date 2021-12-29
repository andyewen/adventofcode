heightmap = []

with open('input.txt') as f:
    for line in f:
        line = line.rstrip('\n')
        heightmap.append([int(c) for c in line])

num_rows = len(heightmap)
num_cols = len(heightmap[0])
    
low_point_coords = []
basin_sizes = []

for j in range(num_rows):
    for i in range(num_cols):
        height = heightmap[j][i]

        # Check horizontally adjacent.
        if i > 0 and heightmap[j][i - 1] <= height:
            continue
        if i < num_cols - 1 and heightmap[j][i + 1] <= height:
            continue

        # Check vertically adjacent.
        if j > 0 and heightmap[j - 1][i] <= height:
            continue
        if j < num_rows - 1 and heightmap[j + 1][i] <= height:
            continue

        low_point_coords.append((i, j))


basin_sizes = []


for low_point_x, low_point_y in low_point_coords:
    # TODO: Make this fill algorithm actually work...
    w_set = [(low_point_x, low_point_y)]
    visited = []
    while w_set:
        current = w_set.pop()
        visited.append(current)
        x, y = current

        neighbours = []
        for i in range(-1, 2):
            if not 0 < x + i < num_cols - 1:
                continue
            neighbours.append((x + i, y))

        for j in range(-1, 2):
            if not 0 < y + j < num_rows - 1:
                continue
            neighbours.append((x, y + j))

        for neighbour in neighbours:
            if (
                heightmap[y][x] < heightmap[neighbour[1]][neighbour[0]] < 9 
                and neighbour not in visited
            ):
                w_set.append(neighbour)

    basin_sizes.append(len(set(visited)))

basin_sizes.sort(reverse=True)

print(basin_sizes[0] * basin_sizes[1] * basin_sizes[2])
