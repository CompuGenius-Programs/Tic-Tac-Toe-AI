class BaseEngine:
    def __init__(self):
        self.wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        self.board = [' ' for _ in range(9)]
        self.turn = 'X'
        self.won = ''

    def display(self):
        board = self.board
        print(f'{board[0]} | {board[1]} | {board[2]}\n'
              f'---------\n'
              f'{board[3]} | {board[4]} | {board[5]}\n'
              f'---------\n'
              f'{board[6]} | {board[7]} | {board[8]}')

    def check_for_end(self):
        for win in self.wins:
            line = [self.board[i] for i in win]
            if line.count('X') == 3:
                self.won = 'X'
                break
            elif line.count('O') == 3:
                self.won = 'O'
                break
        if self.won == '' and ' ' not in self.board:
            self.won = 'Tie!'

    def ai_turn(self):
        # TODO Implement the AI logic here
        move = -1
        return move

    def player_turn(self):
        self.display()

        move = -1
        while move not in range(9) or self.board[move] != ' ':
            try:
                move = int(input('Enter a number between 0 and 8: '))
                if move not in range(9) or self.board[move] != ' ':
                    print('Invalid move. Try again.')
            except ValueError:
                print('Invalid move. Try again.')
        return move

    def game_turn(self):
        if self.turn == 'X':
            move = self.player_turn()
        else:
            move = self.ai_turn()

        self.board[move] = self.turn
        self.turn = 'O' if self.turn == 'X' else 'X'

        self.check_for_end()
        if self.won == '':
            self.game_turn()
        else:
            self.display()
            print(f'{self.won} won!' if self.won != 'Tie!' else 'It\'s a Tie!')
