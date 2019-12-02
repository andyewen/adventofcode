with open('input.txt') as f:
    file_contents = f.read()

instructions = file_contents.split(',')
instructions = [int(i) for i in instructions]

instructions[1] = 12
instructions[2] = 2

position = 0
while 1:
    opcode = instructions[position]
    if opcode == 99:
        break

    a = instructions[position + 1]
    b = instructions[position + 2]
    dest = instructions[position + 3]

    result = None
    if opcode == 1:
        result = instructions[a] + instructions[b]
    elif opcode == 2:
        result = instructions[a] * instructions[b]

    instructions[dest] = result
    position += 4

print(instructions)
