with open('input.txt') as f:
    line = f.readline().rstrip()
    fish_ages = [int(i) for i in line.split(',')]

for day in range(80):
    spawn_count = 0
    for idx, age in enumerate(fish_ages):
        if age > 0:
            fish_ages[idx] -= 1
        else:
            spawn_count += 1
            fish_ages[idx] = 6

    fish_ages.extend([8] * spawn_count)

print(len(fish_ages))
