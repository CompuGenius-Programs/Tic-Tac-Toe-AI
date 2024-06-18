wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]


def initialize_game():
    board = [' ' for _ in range(9)]
    turn = 'X'
    won = ''
    return board, turn, won


def check_for_win(board):
    won = ''
    position = -1

    for win in wins:
        line = [board[i] for i in win]
        if line.count('X') == 3:
            won = 'X'
            break
        elif line.count('O') == 3:
            won = 'O'
            break
        elif 2 in [line.count('X'), line.count('O')] and ' ' in line:
            position = win[line.index(' ')]
            break

    if won == '' and ' ' not in board:
        won = 'Tie!'
    return won, position


def get_next_best_move(board):
    box_wins = [0 for _ in range(9)]
    o_wins = [[board[box] for box in win] for win in wins if
              'O' in [board[box] for box in win] and 'X' not in [board[box] for box in win]]
    for win in o_wins:
        for box in win:
            for row in wins:
                if box in row and 'X' in [board[n] for n in row] and board[box] == ' ':
                    box_wins[box] += 1
    if box_wins == box_wins[::-1] and 2 in box_wins:
        box_wins = [0 if n == 2 else n for n in box_wins]
    return box_wins.index(max(box_wins)) if box_wins != [0 for _ in range(9)] else -1


def game_turn(board, turn, won):
    if turn == 'X':
        move = get_player_turn(board)
        board[move] = 'X'
        turn = 'O'
    else:
        if 'O' not in board:
            move = 4 if board[4] == ' ' else 0
        else:
            won, move = check_for_win(board)
            if won == '':
                if move == -1:
                    move = get_next_best_move(board)
                    if move == -1:
                        move = board.index(' ') if ' ' in board else -1
                        won = 'Tie!' if move == -1 else ''
        if won == '':
            board[move] = 'O'
            turn = 'X'

    won, _ = check_for_win(board)
    if won == '':
        game_turn(board, turn, won)
    else:
        display(board)
        print(f'{won} won!' if won != 'Tie!' else 'It\'s a Tie!')


def get_player_turn(board):
    display(board)

    move = -1
    while move not in range(9) or board[move] != ' ':
        try:
            move = int(input('Enter a number between 0 and 8: '))
        except ValueError:
            print('Invalid input. Try again.')
    return move


def display(board):
    print(f'{board[0]} | {board[1]} | {board[2]}\n'
          f'---------\n'
          f'{board[3]} | {board[4]} | {board[5]}\n'
          f'---------\n'
          f'{board[6]} | {board[7]} | {board[8]}')


def main():
    board, turn, won = initialize_game()
    game_turn(board, turn, won)


if __name__ == '__main__':
    main()
