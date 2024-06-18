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
    if won == '':
        for win in wins:
            line = [board[i] for i in win]
            if line.count('O') == 2 and ' ' in line:
                position = win[line.index(' ')]
                break
    if won == '' and position == -1:
        for win in wins:
            line = [board[i] for i in win]
            if line.count('X') == 2 and ' ' in line:
                position = win[line.index(' ')]
                break

    if won == '' and ' ' not in board:
        won = 'Tie!'
    return won, position


def get_next_best_move(board):
    box_wins = [0 for _ in range(9)]
    pos = 0
    o_wins = [win for win in wins if 'O' in [board[box] for box in win] and 'X' not in [board[box] for box in win]]
    for win in o_wins:
        for box in win:
            for row in wins:
                if box in row and 'X' in [board[n] for n in row] and board[box] == ' ':
                    box_wins[box] += 1
    if box_wins == box_wins[::-1] and 2 in box_wins:
        box_wins = [(box_wins[n] if box_wins[n] != 2 else 0) for n in range(9)]
    if box_wins != [0 for _ in range(9)]:
        pos = box_wins.index(max(box_wins))
    return pos


def game_turn(board, turn, won):
    if turn == 'X':
        move = get_player_turn(board)
        board[move] = 'X'
        turn = 'O'
    else:
        if 'O' not in board:
            move = 4 if board[4] == ' ' else 0
            print("Got move from \"first move\"")
        else:
            won, move = check_for_win(board)
            if won == '':
                if move != -1:
                    print("Got move from \"check_for_win\"")
                else:
                    move = get_next_best_move(board)
                    if move != -1:
                        print("Got move from \"get_next_best_move\"")
                    else:
                        move = board.index(' ') if ' ' in board else -1
                        print("Got move from \"last empty space\"")
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
            if move not in range(9) or board[move] != ' ':
                print('Invalid move. Try again.')
        except ValueError:
            print('Invalid move. Try again.')
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
