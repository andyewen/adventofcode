#!/usr/bin/env python3
import sys

if len(sys.argv) > 1:
    s = sys.argv[1]
else:
    with open('input_files/1.txt') as f:
        s = f.read()
    s = s.strip()

sum = 0
for i in range(len(s)):
    if s[i] == s[(i + len(s) // 2) % len(s)]:
        n = int(s[i])
        sum += n

print(sum)
