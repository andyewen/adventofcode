word = 'MAS'
reversed_word = word[::-1]

grid = []
with open('input.txt') as in_file:
    for line in in_file:
        line = line.strip()
        grid.append(list(line))

width = len(grid[0])
height = len(grid)

count_mas = 0

for subgrid_y in range(height - len(word) + 1):
    for subgrid_x in range(width - len(word) + 1):
        stroke_a = ''.join((
            grid[subgrid_y][subgrid_x],
            grid[subgrid_y + 1][subgrid_x + 1],
            grid[subgrid_y + 2][subgrid_x + 2],
        ))

        stroke_b = ''.join((
            grid[subgrid_y + 2][subgrid_x],
            grid[subgrid_y + 1][subgrid_x + 1],
            grid[subgrid_y][subgrid_x + 2],
        ))
        
        count_mas += (
            (stroke_a == word or stroke_a == reversed_word)
            and (stroke_b == word or stroke_b == reversed_word)
        )

print(count_mas)
