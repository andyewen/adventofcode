import itertools

with open('input.txt') as f:
    file_contents = f.read()

program = file_contents.split(',')
program = [int(instruction) for instruction in program]


def do_program(program):
    position = 0
    while 1:
        opcode = program[position]
        if opcode == 99:
            break

        a, b, dest = program[position + 1:position + 4]

        result = None
        if opcode == 1:
            result = program[a] + program[b]
        elif opcode == 2:
            result = program[a] * program[b]

        program[dest] = result
        position += 4


for a, b in itertools.product(range(100), range(100)):
    program_copy = program[:]
    program_copy[1] = a
    program_copy[2] = b
    do_program(program_copy)
    result = program_copy[0]
    if result == 19690720:
        break

print(f'Noun: {a}, Verb: {b}')
