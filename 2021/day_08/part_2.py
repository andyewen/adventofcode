segments_to_digit = {
    'abcefg': 0,
    'cf': 1,
    'acdeg': 2,
    'acdfg': 3,
    'bcdf': 4,
    'abdfg': 5,
    'abdefg': 6,
    'acf': 7,
    'abcdefg': 8,
    'abcdfg': 9,
}

with open('input.txt') as f:
    for line in f:
        line = line.rstrip('\n')
        inputs, outputs = line.split(' | ', maxsplit=1)
        inputs = inputs.split()
        outputs = outputs.split()
        print(inputs)
        print(outputs)
        print()
