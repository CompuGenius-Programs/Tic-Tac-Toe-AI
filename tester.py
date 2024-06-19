import datetime
import multiprocessing
import random
import time

import engine


def play_game(game_id):
    x_turns = []

    game_engine = engine.Engine()

    while game_engine.won == '':
        if game_engine.turn == 'X':
            valid_moves = [i for i, space in enumerate(game_engine.board) if space == ' ']
            move = random.choice(valid_moves)
            x_turns.append(move)
        else:
            move = game_engine.ai_turn(True)

        game_engine.board[move] = game_engine.turn
        game_engine.turn = 'O' if game_engine.turn == 'X' else 'X'
        game_engine.check_for_end()
    return game_engine.won, x_turns


def play_games(threads):
    with multiprocessing.Pool() as pool:
        games = pool.map(play_game, range(threads))
    return games


if __name__ == '__main__':
    # I have an AMD Ryzen 9 7900X with 12 cores and 24 threads and 64GB of RAM.
    # LOWER THIS NUMBER SIGNIFICANTLY IF YOU HAVE LESS RESOURCES.
    num_games = 10_000_000

    start_time = time.time()
    results = play_games(num_games)
    end_time = time.time()

    winners = [result[0] for result in results]
    print(f'Won: {winners.count("O")} - Lost {winners.count("X")} - Tied {winners.count("Tie!")}')

    if winners.count('X') > 0:
        games_x_won = [result[1] for result in results if result[0] == 'X']
        print(f'X\'s moves in games it won: {games_x_won}')
    else:
        print('Seems pretty unbeatable!')

    print(f'Tested {num_games} games in {datetime.timedelta(seconds=end_time - start_time)}')
