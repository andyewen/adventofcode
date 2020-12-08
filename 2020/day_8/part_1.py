with open('input.txt') as f:
    instructions = []
    for line in f:
        line = line.rstrip('\n')
        operation, argument = line.split(maxsplit=1)
        argument = int(argument)
        instructions.append((operation, argument))

lines_executed = set()
current_line = 0
accumulator = 0
while True:
    operation, argument = instructions[current_line]

    if current_line in lines_executed:
        print(accumulator)
        break

    lines_executed.add(current_line)

    increment = 1

    if operation == 'acc':
        accumulator += argument
    elif operation == 'jmp':
        increment = argument
    
    current_line += increment
