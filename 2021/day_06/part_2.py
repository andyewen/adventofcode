from collections import deque

with open('input.txt') as f:
    line = f.readline()

line = line.rstrip('\n')
fish_ages = [int(i) for i in line.split(',')]

generations = deque(0 for _ in range(9))
for age in fish_ages:
    generations[age] += 1

for day in range(256):
    spawning_count = generations.popleft()
    generations.append(spawning_count)
    generations[6] += spawning_count

print(sum(generations))
