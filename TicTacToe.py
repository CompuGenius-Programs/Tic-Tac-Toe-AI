import random
import time

import pygame

pygame.init()
window = pygame.display.set_mode((600, 600))
font = pygame.font.Font('C:\\WINDOWS\\Fonts\\comic.ttf', 100)
list_of_coords = [(60 + 200 * m, 25 + 200 * n) for m in range(3) for n in range(3)]


def set_game_colors():
    values = [0, 0, 0]
    for c in range(len(values)):
        values[c] = random.randrange(0, 255)
    window.fill(values)
    pygame.display.update()


def event_grabber():
    for event in pygame.event.get():
        if event == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()


def display():
    global turn, board, move

    def cmp(var, val1=200, val2=400):
        if var <= val1:
            return 0
        elif val1 < var <= val2:
            return 1
        else:
            return 2

    draw_board()
    went = 0
    while not went:
        for event in pygame.event.get():
            event_grabber()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                move = cmp(x) * 3 + cmp(y)
                if board[move] == ' ':
                    img = font.render(turn, 1, (255, 255, 255))
                    window.blit(img, list_of_coords[move])
                    went = 1
                    pygame.display.update()


def ttt_ai():
    global won, board, turn, move
    board = [' ' for _ in range(9)]
    turn = 'X'
    won = ''

    def count(let='', num=3):
        global turn, won, board, pos
        wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
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
                cnt = count_x if let == 'X' else count_o
                if cnt == num and count_n:
                    pos = win[[board[n] for n in win].index(' ')] + 1
                    return pos
        if won == '' and ' ' not in board:
            won = 'Tie!'

    def map_wins():
        global board, pos
        wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
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

    while won == '':
        event_grabber()
        if turn == 'X':
            display()
            board[move] = 'X'
            turn = 'O'
        else:
            move = -1
            if 'O' not in board:
                move = 4
                if board[4] == 'X':
                    move = 0
            else:
                for letter in ['O', 'X']:
                    pos = count(letter, 2)
                    if pos:
                        break
                if pos:
                    move = pos - 1
                elif map_wins():
                    move = map_wins() - 1
                elif ' ' in board:
                    move = board.index(' ')
                else:
                    won = 'Tie!'
            if move >= 0:
                board[move] = 'O'
            img = font.render(turn, 1, (255, 255, 255))
            window.blit(img, list_of_coords[move])
            pygame.display.update()
            turn = 'X'
        count()
    if len(won) == 1:
        display_text("You lost.", (255, 0, 0))
    else:
        display_text("You Tied!", (0, 0, 255))
    event_grabber()


def draw_board():
    values = [0, 0, 0]
    for c in range(len(values)):
        values[c] = random.randrange(0, 255)
    for n in range(1, 3):
        pygame.draw.line(window, values, (200 * n, 0), (200 * n, 600), 5)
        pygame.draw.line(window, values, (0, 200 * n), (600, 200 * n), 5)
    pygame.display.update()


def flash_border_animation(animationSpeed=30):
    time.sleep(1)
    flash_surface = pygame.Surface(window.get_size())
    flash_surface = flash_surface.convert_alpha()
    for start, end, step in ((0, 256, 1), (255, 0, -1)):
        for transparency in range(start, end, animationSpeed * step):
            values = [0, 0, 0, 0]
            for c in range(len(values)):
                values[c] = random.randrange(0, 255)
            flash_surface.fill(values)
            window.blit(flash_surface, (0, 0))
            pygame.display.update()


def display_text(text, color):
    event_grabber()
    flash_border_animation()
    msg = font.render(text, 1, color)
    window.blit(msg, (600 / 2 - 200, 600 / 2 - 100))
    pygame.display.update()
    time.sleep(1)
    set_game_colors()


if __name__ == '__main__':
    set_game_colors()
    while 1:
        ttt_ai()
