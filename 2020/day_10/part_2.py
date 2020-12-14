with open('input.txt') as f:
    adapter_ratings = [int(line.rstrip('\n')) for line in f]

adapter_ratings.sort()
adapter_ratings.insert(0, 0)
adapter_ratings.append(adapter_ratings[-1] + 3)

adj_list = {num: [] for num in adapter_ratings}

for i, num in enumerate(adapter_ratings):
    candidate_index = i + 1
    while candidate_index < len(adapter_ratings):
        candidate = adapter_ratings[candidate_index]
        difference = candidate - num
        if 1 <= difference <= 3:
            adj_list[num].append(candidate)
            candidate_index += 1
        else:
            break


ways_to_end_by_adapter = {}
for num in reversed(adapter_ratings):
    if num == adapter_ratings[-1]:
        ways_to_end_by_adapter[num] = 1
    else:
        ways_to_end_by_adapter[num] = sum(ways_to_end_by_adapter[adapter] for adapter in adj_list[num])


print(ways_to_end_by_adapter[0])
