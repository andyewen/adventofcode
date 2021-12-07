from collections import defaultdict

grid = defaultdict(int)

with open('input.txt') as f:
    for line in f:
        line = line.rstrip('\n')
        a, _, b = line.split()
        a = tuple(int(n) for n in a.split(','))
        b = tuple(int(n) for n in b.split(','))

        # if a[0] != b[0] and a[1] != b[1]:
        #     # Skip diagonals.
        #     continue

        while True:
            # Walk the line!
            grid[a] += 1

            if a != b:
                if a[0] < b[0]:
                    a = (a[0] + 1, a[1])
                elif a[0] > b[0]:
                    a = (a[0] - 1, a[1])

                if a[1] < b[1]:
                    a = (a[0], a[1] + 1)
                elif a[1] > b[1]:
                    a = (a[0], a[1] - 1)
            else:
                break

print(sum(v > 1 for v in grid.values()))
