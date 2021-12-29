heightmap = []

with open('input.txt') as f:
    for line in f:
        line = line.rstrip('\n')
        heightmap.append([int(c) for c in line])

num_rows = len(heightmap)
num_cols = len(heightmap[0])
    
lowest_sum = 0

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

        # print(height)
        lowest_sum += height + 1

# print()
print(lowest_sum)
