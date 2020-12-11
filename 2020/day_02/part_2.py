import re

line_regex = re.compile(r'(\d+)\-(\d+) (\w): (\w+)')

valid_passwords = 0

with open('input.txt') as f:
    for line in f:
        line = line.rstrip('\n')
        match = line_regex.match(line)
        index_1 = int(match.group(1))
        index_2 = int(match.group(2))
        character = match.group(3)
        password = match.group(4)

        valid_passwords += int(
            (password[index_1 - 1] == character) != (password[index_2 - 1] == character)
        )

print(valid_passwords)
