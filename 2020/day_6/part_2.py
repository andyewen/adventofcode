def get_grouped_lines(file):
    current_group = []
    for line in file:
        line = line.rstrip('\n')
        if line:
            current_group.append(line)
        else:
            if current_group:
                yield current_group
            current_group = []
    if current_group:
        yield current_group


with open('input.txt') as f:
    total = 0
    for group in get_grouped_lines(f):
        group_questions = set(group[0])
        for line in group[1:]:
            group_questions &= set(line)
        total += len(group_questions)

print(total)
