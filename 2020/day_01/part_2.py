import itertools

with open('input.txt') as f:
    numbers = [
        int(line.strip()) for line in f
    ]

for nums in itertools.combinations(numbers, 3):
    if sum(nums) == 2020:
        product = 1
        for n in nums:
            product *= n
        print(product)
        break
