unique_lengths = {2, 4, 3, 7}
count = 0

with open('input.txt') as f:
    for line in f:
        line = line.rstrip('\n')
        _, outputs = line.split(' | ', maxsplit=1)
        outputs = outputs.split()
        for o in outputs:
            if len(o) in unique_lengths:
                count += 1

print(count)
