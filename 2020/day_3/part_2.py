import math

def count_tree_collisions(dx, dy):
    with open('input.txt') as f:
        trees_hit = 0
        x_pos = 0
        for y_pos, line in enumerate(f):
            if y_pos % dy != 0:
                continue
            line = line.rstrip('\n')
            trees_hit += int(line[x_pos] == '#')
            x_pos = (x_pos + dx) % len(line)
    return trees_hit

angles = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]

print(math.prod(count_tree_collisions(*angle) for angle in angles))
