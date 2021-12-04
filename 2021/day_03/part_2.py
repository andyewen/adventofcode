line_length = 12

with open('input.txt') as f:
    lines = [line.rstrip('\n') for line in f]

def calculate_gamma_and_epsilon(numbers):
    column_sums = [0 for _ in range(line_length)]
    for n in numbers:
        for idx in range(line_length):
            column_sums[idx] += int(n[idx])

    gamma = ''
    epsilon = ''
    for c_sum in column_sums:
        ones = c_sum
        zeroes = len(numbers) - c_sum
        if ones >= zeroes:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'
        
    return gamma, epsilon

o2_candidates = list(lines)
co2_candidates = list(lines)
for idx in range(12):
    checking_o2 = len(o2_candidates) > 1
    checking_co2 = len(co2_candidates) > 1
    if not checking_o2 and not checking_co2:
        break
    if checking_o2:
        gamma, epsilon = calculate_gamma_and_epsilon(o2_candidates)
        filtered_o2_candidates = []
        for o2_cand in o2_candidates:
            if o2_cand[idx] == gamma[idx]:
                filtered_o2_candidates.append(o2_cand)
        o2_candidates = filtered_o2_candidates
    if checking_co2:
        gamma, epsilon = calculate_gamma_and_epsilon(co2_candidates)
        filtered_co2_candidates = []
        for co2_cand in co2_candidates:
            if co2_cand[idx] == epsilon[idx]:
                filtered_co2_candidates.append(co2_cand)
        co2_candidates = filtered_co2_candidates


print(int(o2_candidates[0], 2) * int(co2_candidates[0], 2))


    
