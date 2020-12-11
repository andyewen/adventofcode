def find_binary(l, low, high):
    for b in l:
        middle = (high + low) // 2
        if b:
            low = middle
        else:
            high = middle
    return low

all_seat_ids = set(i for i in range(0, 127 * 8 + 7))
seen_seat_ids = set()

with open('input.txt') as f:
    for line in f:
        line = line.rstrip('\n')
        
        row_part = [c == 'B' for c in line[:7]]
        row_number = find_binary(row_part, 0, 128)

        column_part = [c == 'R' for c in line[7:]]
        column_number = find_binary(column_part, 0, 8)

        seat_id = row_number * 8 + column_number
        seen_seat_ids.add(seat_id)

print(all_seat_ids - seen_seat_ids)
