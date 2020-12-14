import collections

with open('input.txt') as f:
    adapter_ratings = [int(line.rstrip('\n')) for line in f]

jumps = collections.Counter()

adapter_ratings.sort()

visited = set()
current_rating = 0
while True:
    next_rating = None
    for other_rating in adapter_ratings:
        difference = other_rating - current_rating
        if other_rating not in visited and 1 <= difference <= 3:
            next_rating = other_rating
            visited.add(other_rating)
            jumps[difference] += 1
            break
    if next_rating is None:
        break
    else:
        current_rating = next_rating

jumps[3] += 1

print(jumps)
print(jumps[1] * jumps[3])
