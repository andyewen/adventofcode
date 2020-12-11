import re

line_regex = re.compile(r'(\d+)\-(\d+) (\w): (\w+)')

valid_passwords = 0

with open('input.txt') as f:
    for line in f:
        line = line.rstrip('\n')
        match = line_regex.match(line)
        min_count = int(match.group(1))
        max_count = int(match.group(2))
        character = match.group(3)
        password = match.group(4)

        count = sum(c == character for c in password)
        valid_passwords += int(min_count <= count <= max_count)

print(valid_passwords)
