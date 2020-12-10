import collections
import itertools

target_number = 22406676
numbers = []

with open('input.txt') as f:
    for line in f:
        n = int(line.rstrip('\n'))
        numbers.append(n)


for i in range(len(numbers)):
    result = None
    for j in range(i + 1, len(numbers)):
        chunk = numbers[i:j]
        total = sum(chunk)
        if total == target_number:
            minimum = min(chunk)
            maximum = max(chunk)
            result = minimum + maximum
            break
        elif total >= target_number:
            # We have exceeded. Can skip the rest of this chunk.
            break

    if result is not None:
        print(result)
        break
