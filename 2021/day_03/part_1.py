line_length = 12
column_sums = [0 for _ in range(line_length)]
num_lines = 0

with open('input.txt') as f:
    for line in f:
        num_lines += 1
        line = line.rstrip('\n')

        for idx in range(line_length):
            column_sums[idx] += int(line[idx])

gamma = ''
epsilon = ''
for c_sum in column_sums:
    if c_sum > num_lines // 2:
        gamma += '1'
        epsilon += '0'
    else:
        gamma += '0'
        epsilon += '1'

gamma_as_decimal = int(gamma, base=2)
epsilon_as_decimal = int(epsilon, base=2)

print(f'Gamma: {gamma}b, {gamma_as_decimal}d')
print(f'Epsilon: {epsilon}b, {epsilon_as_decimal}d')

print(f'gamma * decimal = {gamma_as_decimal * epsilon_as_decimal}')
