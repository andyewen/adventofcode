safe_count = 0

with open('input.txt') as in_file:
    for line in in_file:
        line = line.rstrip('\n')

        nums = [int(n) for n in line.split()]

        differences = [next - curr for curr, next in zip(nums[:-1], nums[1:])]

        safe_count += (
            all(-3 <= d <= -1 for d in differences)
            or all(1 <= d <= 3 for d in differences)
        )

print(safe_count)
