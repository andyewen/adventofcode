from functools import cmp_to_key

rules = set()

def comparator(a, b):
    if (a, b) in rules:
        return -1
    if (b, a) in rules:
        return 1
    return 0

result = 0

with open('input.txt') as in_file:
    for line in in_file:
        line = line.rstrip('\n')
        if not line:
            break
        rules.add(tuple(int(n) for n in line.split('|')))
        
    for line in in_file:
        numbers = [int(n) for n in line.split(',')]
        if numbers == sorted(numbers, key=cmp_to_key(comparator)):
            result += numbers[len(numbers) // 2]

print(result)
