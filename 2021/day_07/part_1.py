def alignment_fuel(pos, crab_positions):
    return sum(abs(crab_pos - pos) for crab_pos in crab_positions)


with open('input.txt') as f:
    crab_positions = [int(i) for i in f.readline().rstrip().split(',')]

min_pos = min(crab_positions)
max_pos = max(crab_positions)

min_fuel = min(alignment_fuel(pos, crab_positions) for pos in range(min_pos, max_pos + 1))
print(min_fuel)
