with open('input.txt') as f:
    numbers = [int(line.strip()) for line in f]

previous_window_sum = None
increasing_count = 0
for idx in range(0, len(numbers) - 2):
    window = numbers[idx:idx+3]
    window_sum = sum(window)
    if previous_window_sum is not None and window_sum > previous_window_sum:
        increasing_count += 1
    previous_window_sum = window_sum

print(increasing_count)
