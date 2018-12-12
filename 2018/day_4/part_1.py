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


def sum_sleep_times(sleep_time_list):
    return sum(sleep['end'] - sleep['start'] for sleep in sleep_time_list)


guard_id, sleep_stats = max(guard_sleep_times.items(), key=lambda p: sum_sleep_times(p[1]))
print(f'Guard #{guard_id} slept for {sum_sleep_times(sleep_stats)}, the longest of any guard.')

per_minute_stats = [0] * 60
for sleep in sleep_stats:
    for m in range(sleep['start'], sleep['end']):
        per_minute_stats[m] += 1

max_minute = per_minute_stats.index(max(per_minute_stats))
print(f'They slept most during minute {max_minute}.')
