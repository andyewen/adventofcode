def find_binary(l, low, high):
    for b in l:
        middle = (high + low) // 2
        if b:
            low = middle
        else:
            high = middle
    return low

with open('input.txt') as f:
    max_seat_id = None
    for line in f:
        line = line.rstrip('\n')
        row_part = [c == 'B' for c in line[:7]]
        row_number = find_binary(row_part, 0, 128)
        column_part = [c == 'R' for c in line[7:]]
        column_number = find_binary(column_part, 0, 8)
        seat_id = row_number * 8 + column_number
        if max_seat_id is None or seat_id > max_seat_id:
            max_seat_id = seat_id

print(max_seat_id)
