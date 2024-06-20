import base_engine


class OriginalEngine(base_engine.BaseEngine):
    def check_for_win(self, let=''):
        won = ''
        pos = -1

        for win in self.wins:
            count_x, count_o, count_n = 0, 0, 0
            for box in win:
                if self.board[box] == 'O':
                    count_o += 1
                elif self.board[box] == 'X':
                    count_x += 1
                else:
                    count_n += 1
            count = count_x if let == ('X' if self.playing_as == 'O' else 'O') else count_o
            if count == 2 and count_n:
                pos = win[[self.board[n] for n in win].index(' ')]
                return won, pos
        if won == '' and ' ' not in self.board:
            won = 'Tie!'

        return won, pos

    def get_next_best_move(self):
        box_wins = [0 for _ in range(9)]
        pos = 0
        o_wins = []
        for win in self.wins:
            board_array = [self.board[box] for box in win]
            if self.playing_as in board_array and ('X' if self.playing_as == 'O' else 'O') not in board_array:
                o_wins.append(win)
        for win in o_wins:
            for box in win:
                for row in self.wins:
                    if box in row and ('X' if self.playing_as == 'O' else 'O') in [self.board[n] for n in row] and self.board[box] == ' ':
                        box_wins[box] += 1
        if box_wins == box_wins[::-1] and 2 in box_wins:
            box_wins = [(box_wins[n] if box_wins[n] != 2 else 0) for n in range(9)]
        if box_wins != [0 for _ in range(9)]:
            pos = box_wins.index(max(box_wins))
        return pos

    def ai_turn(self, testing=False):
        if self.playing_as not in self.board:
            # move = 4
            # if self.board[4] != ' ':
            #     move = 0
            move = 4 if self.board[4] == ' ' else 0
            if not testing:
                print("Got move from \"first move\"")
        else:
            for letter in ['O', 'X'] if self.playing_as == 'O' else ['X', 'O']:
                won, move = self.check_for_win(letter)
                if move != -1:
                    break
            if move != -1:
                if not testing:
                    print("Got move from \"check_for_win\"")
            else:
                move = self.get_next_best_move()
                if move != -1:
                    if not testing:
                        print("Got move from \"get_next_best_move\"")
                elif ' ' in self.board:
                    move = self.board.index(' ')
                    if not testing:
                        print("Got move from \"last empty space\"")

        return move
