def print_board(board):
    for row in winning_board:
        print(' '.join(f'{num:>2}' for num in row))


def board_is_winner(board, drawn_numbers):
    drawn_numbers = set(drawn_numbers)
    for row in board:
        if all(n in drawn_numbers for n in row):
            # Row is winner!
            return True
    
    for col_idx in range(len(board[0])):
        if all(row[col_idx] in drawn_numbers for row in board):
            # Column is winner!
            return True

    return False


def board_score(board, drawn_numbers):
    drawn_numbers = set(drawn_numbers)
    score = 0
    for row in board:
        for num in row:
            if num not in drawn_numbers:
                score += num
    return score


boards = []

with open('input.txt') as f:
    first_line = f.readline().rstrip('\n')
    random_numbers = [int(i) for i in first_line.split(',')]

    board = []
    for line in f:
        line = line.rstrip()
        if line:
            line_numbers = []
            for i in range(0, len(line), 3):
                line_numbers.append(int(line[i:i+3]))
            board.append(line_numbers)

        # Board complete! Append it and reset for the next incoming board.
        if len(board) >= 5:
            boards.append(board)
            board = []

winning_board = None
winning_number = None
drawn_numbers = set()
for num in random_numbers:
    drawn_numbers.add(num)

    if len(boards) == 1 and board_is_winner(boards[0], drawn_numbers):
        winning_board = boards[0]
        winning_number = num
        break
    
    boards = [board for board in boards if not board_is_winner(board, drawn_numbers)]

print_board(winning_board)
print()
winning_board_score = board_score(winning_board, drawn_numbers)
print(f'Score: {winning_board_score}')
print(f'Number: {winning_number}')

answer = winning_board_score * winning_number
print(f'Answer: {answer}')
