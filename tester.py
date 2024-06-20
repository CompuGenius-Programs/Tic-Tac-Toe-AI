import datetime
import multiprocessing
import time

import engine


def play_game(game_id, ai_plays_as):
    x_turns = []

    game_engine = engine.Engine()
    game_engine.playing_as = ai_plays_as

    old_engine = engine.OriginalEngine()
    old_engine.playing_as = 'X' if ai_plays_as == 'O' else 'O'

    while game_engine.won == '':
        if game_engine.turn == ai_plays_as:
            move = game_engine.ai_turn(True)
        else:
            move = old_engine.ai_turn(True)
            # valid_moves = [i for i, space in enumerate(game_engine.board) if space == ' ']
            # move = random.choice(valid_moves)
            x_turns.append(move)

        game_engine.board[move] = game_engine.turn
        game_engine.turn = 'O' if game_engine.turn == 'X' else 'X'
        game_engine.check_for_end()

        old_engine.board[move] = game_engine.turn
        old_engine.turn = 'O' if game_engine.turn == 'X' else 'X'
    return game_engine.won, x_turns


def play_games(threads):
    with multiprocessing.Pool() as pool:
        games = pool.starmap(play_game, [(game_id, ai_plays_as) for game_id in range(threads)])
    return games


if __name__ == '__main__':
    # I have an AMD Ryzen 9 7900X with 12 cores and 24 threads and 64GB of RAM.
    # LOWER THIS NUMBER SIGNIFICANTLY IF YOU HAVE LESS RESOURCES.
    num_games = 10_000_000

    ai_plays_as = 'X'

    start_time = time.time()
    results = play_games(num_games)
    end_time = time.time()

    winners = [result[0] for result in results]
    print(
        f'AI Won: {winners.count(ai_plays_as)} - Lost {winners.count("X" if ai_plays_as == "O" else "O")} - Tied {winners.count("Tie!")}')

    if winners.count("X" if ai_plays_as == "O" else "O") > 0:
        games_tester_won = [result[1] for result in results if result[0] == ("X" if ai_plays_as == "O" else "O")]
        print(f'{"X" if ai_plays_as == "O" else "O"}\'s moves in games it won: {games_tester_won}')
    else:
        print('Seems pretty unbeatable!')

    print(f'Tested {num_games} games in {datetime.timedelta(seconds=end_time - start_time)}')
