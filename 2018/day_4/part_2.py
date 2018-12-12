#!/usr/bin/env python3
import re
from collections import defaultdict

with open('input.txt') as fp:
    lines = list(fp)

lines.sort()

guard_sleep_times = defaultdict(list)
current_guard = None
sleep_start = None

for l in lines:
    minute = int(l[15:17])
    message = l[19:-1]

    m = re.match(r'Guard #(\d+)', message)
    if m:
        current_guard = int(m.group(1))
    elif message == 'falls asleep':
        sleep_start = minute
    elif message == 'wakes up':
        guard_sleep_times[current_guard].append({'start': sleep_start, 'end': minute})

max_times = 0
max_minute = None
max_guard = None
for guard_id, sleep_times in guard_sleep_times.items():
    per_minute_stats = [0] * 60
    for sleep in sleep_times:
        for m in range(sleep['start'], sleep['end']):
            per_minute_stats[m] += 1

    guard_max_times = max(per_minute_stats)
    if guard_max_times > max_times:
        max_times = guard_max_times
        max_minute = per_minute_stats.index(guard_max_times)
        max_guard = guard_id


print(f'The guard most often asleep during minute {max_minute} was #{max_guard} at {max_times} times.')
