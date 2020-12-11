with open('input.txt') as f:
    instructions = []
    for line in f:
        line = line.rstrip('\n')
        operation, argument = line.split(maxsplit=1)
        argument = int(argument)
        instructions.append((operation, argument))


def execute(instructions, swap_line):
    lines_executed = set()
    current_line = 0
    accumulator = 0
    while current_line < len(instructions):
        if current_line in lines_executed:
            return None
        lines_executed.add(current_line)

        operation, argument = instructions[current_line]
        if current_line == swap_line:
            if operation == 'jmp':
                operation = 'nop'
            elif operation == 'nop':
                operation = 'jmp'

        increment = 1

        if operation == 'acc':
            accumulator += argument
        elif operation == 'jmp':
            increment = argument

        current_line += increment
    return accumulator


for i, (operation, argument) in enumerate(instructions):
    if operation not in {'jmp', 'nop'}:
        # Skip lines we don't swap
        continue

    accumulator = execute(instructions, i)
    if accumulator is not None:
        print(accumulator)
        break
