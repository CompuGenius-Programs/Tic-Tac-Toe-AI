wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]


def initialize_game():
    board = [' ' for _ in range(9)]
    turn = 'X'
    won = ''
    return board, turn, won


def check_for_win(board, let='', num=3):
    won = ''
    pos = -1

    for win in wins:
        count_x, count_o, count_n = 0, 0, 0
        for box in win:
            if board[box] == 'O':
                count_o += 1
            elif board[box] == 'X':
                count_x += 1
            else:
                count_n += 1
        if num == 3:
            if count_x == 3:
                won = 'X'
            if count_o == 3:
                won = 'O'
            if won != '':
                break
        else:
            count = count_x if let == 'X' else count_o
            if count == num and count_n:
                pos = win[[board[n] for n in win].index(' ')] + 1
                return won, pos
    if won == '' and ' ' not in board:
        won = 'Tie!'

    return won, pos


def get_next_best_move(board):
    box_wins = [0 for _ in range(9)]
    pos = 0
    o_wins = []
    for win in wins:
        board_array = [board[box] for box in win]
        if 'O' in board_array and 'X' not in board_array:
            o_wins.append(win)
    for win in o_wins:
        for box in win:
            for row in wins:
                if box in row and 'X' in [board[n] for n in row] and board[box] == ' ':
                    box_wins[box] += 1
    if box_wins == box_wins[::-1] and 2 in box_wins:
        box_wins = [(box_wins[n] if box_wins[n] != 2 else 0) for n in range(9)]
    if box_wins != [0 for _ in range(9)]:
        pos = box_wins.index(max(box_wins)) + 1
    return pos


def game_turn(board, turn):
    if turn == 'X':
        move = get_player_turn(board)
        board[move] = 'X'
        turn = 'O'
    else:
        if 'O' not in board:
            move = 4
            if board[4] == 'X':
                move = 0
            print("Got move from \"first move\"")
        else:
            for letter in ['O', 'X']:
                won, move = check_for_win(board, letter, 2)
                if move != -1:
                    break
            if move != -1:
                move -= 1
                print("Got move from \"check_for_win\"")
            move = get_next_best_move(board)
            if move != 0:
                move -= 1
                print("Got move from \"get_next_best_move\"")
            elif ' ' in board:
                move = board.index(' ')
                print("Got move from \"last empty space\"")
        if move >= 0:
            board[move] = 'O'
        turn = 'X'

    won, _ = check_for_win(board)
    if won == '':
        game_turn(board, turn)
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
    game_turn(board, turn)


if __name__ == '__main__':
    main()
