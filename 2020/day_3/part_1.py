with open('input.txt') as f:
    trees_hit = 0
    x_pos = 0
    for line in f:
        line = line.rstrip('\n')
        trees_hit += int(line[x_pos] == '#')
        x_pos = (x_pos + 3) % len(line)

print(trees_hit)
