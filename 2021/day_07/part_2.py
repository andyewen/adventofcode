def alignment_fuel(pos, crab_positions):
    total_fuel = 0
    for crab_pos in crab_positions:
        delta = abs(crab_pos - pos)
        crab_fuel = (delta * (delta + 1)) // 2  # Sum consecutive numbers.
        total_fuel += crab_fuel
    return total_fuel

with open('input.txt') as f:
    crab_positions = [int(i) for i in f.readline().rstrip().split(',')]

min_pos = min(crab_positions)
max_pos = max(crab_positions)

min_fuel = min(alignment_fuel(pos, crab_positions) for pos in range(min_pos, max_pos + 1))
print(min_fuel)
