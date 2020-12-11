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
    print(sum(
        len(set(''.join(group))) for group in get_grouped_lines(f)
    ))
