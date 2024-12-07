word = 'XMAS'
grid = []
with open('input.txt') as in_file:
    for line in in_file:
        line = line.strip()
        grid.append(list(line))

width = len(grid[0])
height = len(grid)

def find_word(start_x, start_y, direction):
    dx, dy = direction
    match = True
    for i in range(len(word)):
        x = start_x + dx * i
        y = start_y + dy * i
        if (
            x < 0 
            or x >= width 
            or y < 0 
            or y >= height
            or grid[y][x] != word[i]
        ):
            match = False
            break

    return match


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

xmas_count = 0
for y in range(height):
    for x in range(width):
        for direction in directions:
            xmas_count += find_word(x, y, direction)

print(xmas_count)
        
