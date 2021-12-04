with open('input.txt') as f:
    numbers = [int(line.strip()) for line in f]

increasing_count = 0
for idx in range(0, len(numbers) - 1):
    previous, current = numbers[idx:idx+2]
    if current > previous:
        increasing_count += 1

print(increasing_count)
