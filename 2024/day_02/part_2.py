safe_count = 0

def sign(x):
    return (x > 0) - (x < 0)

def sequence_safe(nums):
    differences = [next - curr for curr, next in zip(nums[:-1], nums[1:])]
    return (
        all(-3 <= d <= -1 for d in differences)
        or all(1 <= d <= 3 for d in differences)
    )

def variations(l):
    for i in range(len(l)):
        variation = l[:]  # Copy list to avoid mutating the original.
        del variation[i]
        yield variation

safe_count = 0

with open('input.txt') as in_file:
    for line in in_file:
        line = line.rstrip('\n')

        nums = [int(n) for n in line.split()]

        # Brute force attempt all variations of the list with a single item 
        # removed if the original sequence isn't safe.
        safe_count += (
            sequence_safe(nums)
            or any(
                sequence_safe(v) for v in variations(nums)
            )
        )

print(safe_count)
