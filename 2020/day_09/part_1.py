import collections
import itertools


def validate_number(n, against):
    for a, b in itertools.combinations(against, 2):
        if a + b == n:
            return True
    return False


preamble_length = 25
numbers = collections.deque(maxlen=preamble_length)

with open('input.txt') as f:
    for line in f:
        n = int(line.rstrip('\n'))
        if len(numbers) == preamble_length:
            if not validate_number(n, numbers):
                print(n)
                break

        numbers.append(n)
