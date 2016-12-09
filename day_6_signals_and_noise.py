#!/usr/bin/env python3
from collections import defaultdict
from operator import itemgetter

filename = 'input_files/6.txt'
with open(filename) as inputfile:
    messages = inputfile.read().splitlines()

message_stats = [defaultdict(int) for __ in range(8)]

for m in messages:
    for i, c in enumerate(m):
        message_stats[i][c] += 1

message = ''
for char_stats in message_stats:
    chars = sorted(char_stats.items(), key=itemgetter(0)) 
    chars = sorted(chars, key=itemgetter(1)) 
    if (len(chars)):
        message += chars[0][0]

print(message)
