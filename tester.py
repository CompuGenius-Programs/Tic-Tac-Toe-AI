import datetime
import multiprocessing
import random
import time

import rewrite


def play_game(game_id):
    board, turn, won = rewrite.initialize_game()
    x_turns = []

    while won == '':
        if turn == 'X':
            valid_moves = [i for i, space in enumerate(board) if space == ' ']
            move = random.choice(valid_moves)
            x_turns.append(move)

            board[move] = 'X'
            turn = 'O'
        else:
            if 'O' not in board:
                move = 4 if board[4] == ' ' else 0
            else:
                won, move = rewrite.check_for_win(board)
                if won == '':
                    if move == -1:
                        move = rewrite.get_next_best_move(board)
                        if move == -1:
                            move = board.index(' ') if ' ' in board else -1
                            won = 'Tie!' if move == -1 else ''
            if won == '':
                board[move] = 'O'
                turn = 'X'

        won, _ = rewrite.check_for_win(board)
    return won, x_turns


def play_games(threads):
    with multiprocessing.Pool() as pool:
        games = pool.map(play_game, range(threads))
    return games


if __name__ == '__main__':
    # I have an AMD Ryzen 9 7900X with 12 cores and 24 threads and 64GB of RAM.
    # LOWER THIS NUMBER SIGNIFICANTLY IF YOU HAVE LESS RESOURCES.
    num_games = 1_000_000_000

    start_time = time.time()
    results = play_games(num_games)
    end_time = time.time()

    winners = [result[0] for result in results]
    print(f'AI Won: {winners.count("O")}\nLost {winners.count("X")}\nTied {winners.count("Tie!")}')

    games_x_won = [result[1] for result in results if result[0] == 'X']
    print(f'X\'s moves in games it won: {games_x_won}')

    print(f'Tested {num_games} games in {datetime.timedelta(seconds=end_time - start_time)}')
