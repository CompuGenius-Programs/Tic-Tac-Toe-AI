import base_engine


class NewEngine(base_engine.BaseEngine):
    def check_for_win_or_block(self):
        position = -1

        for win in self.wins:
            line = [self.board[i] for i in win]
            if line.count('O') == 2 and ' ' in line:
                position = win[line.index(' ')]
                break
        if position == -1:
            for win in self.wins:
                line = [self.board[i] for i in win]
                if line.count('X') == 2 and ' ' in line:
                    position = win[line.index(' ')]
                    break

        return position

    def get_next_best_move(self):
        box_wins = [0 for _ in range(9)]
        pos = 0
        o_wins = [win for win in self.wins if 'O' in [self.board[box] for box in win] and 'X' not in [self.board[box] for box in win]]
        for win in o_wins:
            for box in win:
                for row in self.wins:
                    if box in row and 'X' in [self.board[n] for n in row] and self.board[box] == ' ':
                        box_wins[box] += 1
        if box_wins == box_wins[::-1] and 2 in box_wins:
            box_wins = [(box_wins[n] if box_wins[n] != 2 else 0) for n in range(9)]
        if box_wins != [0 for _ in range(9)]:
            pos = box_wins.index(max(box_wins))
        return pos

    def ai_turn(self, testing=False):
        if 'O' not in self.board:
            move = 4 if self.board[4] == ' ' else 0
            if not testing:
                print("Got move from \"first move\"")
        else:
            move = self.check_for_win_or_block()
            if move != -1:
                if not testing:
                    print("Got move from \"check_for_win_or_block\"")
            else:
                move = self.get_next_best_move()
                if move != -1:
                    if not testing:
                        print("Got move from \"get_next_best_move\"")
                else:
                    move = self.board.index(' ')
                    if not testing:
                        print("Got move from \"last empty space\"")

        return move
