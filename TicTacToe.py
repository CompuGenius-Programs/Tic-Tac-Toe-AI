import pygame, time, random
pygame.init()
window = pygame.display.set_mode((600,600), pygame.FULLSCREEN)
font = pygame.font.Font('C:\WINDOWS\Fonts\comic.ttf', 100)
list_of_coords=[(60+200*m,25+200*n) for m in range(3) for n in range(3)]

def resetBoard():
    values = [0, 0, 0]
    for c in range(len(values)):
        values[c] = random.randrange(0, 255)
    window.fill(values)
    pygame.display.update()

def eventgrabber():
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
    def cmp(var,val1=200,val2=400):
        if var<=val1:
            return 0
        elif val1<var<=val2:
            return 1
        else:
            return 2
    drawBoard()
    went=0
    while not went:
        for event in pygame.event.get():
            eventgrabber()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                move=cmp(x)*3+cmp(y)
                if board[move]==' ':
                    img = font.render(turn, 1, (255,255,255))
                    window.blit(img,list_of_coords[move])
                    went=1
                    pygame.display.update()

def tttai():
    global won,board,turn,move
    board=[' ' for _ in range(9)]
    turn='X'
    won=''
    def count(let=0,num=3):
        global turn,won,board
        wins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        for win in wins:
            cntx,cnto,cntn=0,0,0
            for box in win:
                if board[box]=='O':
                    cnto+=1
                elif board[box]=='X':
                    cntx+=1
                else:
                    cntn+=1
            if num==3:
                if cntx==3:
                    won='X'
                if cnto==3:
                    won='O'
                if won!='':
                    break
            else:
                pos=0
                cnt=cntx if let=='X' else cnto
                if cnt==num and cntn:
                    pos=win[[board[n] for n in win].index(' ')]+1
                    return pos
        if won=='' and not ' ' in board:
            won='Tie!'

    def mapwins():
        global board
        wins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        boxwins=[0 for _ in range(9)]
        pos=0
        owins=[]
        for win in wins:
            boardlet=[board[box] for box in win]
            if 'O' in boardlet and not 'X' in boardlet:
                owins.append(win)
        for win in owins:
            for box in win:
                for row in wins:
                    if box in row and 'X' in [board[n] for n in row] and board[box]==' ':
                        boxwins[box]+=1
        if boxwins==boxwins[::-1] and 2 in boxwins:
            boxwins=[(boxwins[n] if boxwins[n]!=2 else 0) for n in range(9)]
        if boxwins!=[0 for _ in range(9)]:
            pos=boxwins.index(max(boxwins))+1
        return pos
    while won=='':
        eventgrabber()
        if turn=='X':
            display()
            board[move]='X'
            turn='O'
        else:
            move=-1
            if not 'O' in board:
                move=4
                if board[4]=='X':
                    move=0
            else:
                for letter in ['O','X']:
                    pos=count(letter,2)
                    if pos:
                        break
                if pos:
                    move=pos-1
                elif mapwins():
                    move=mapwins()-1
                elif ' ' in board:
                    move=board.index(' ')
                else:
                    won='Tie!'
            if move>=0:
                board[move]='O'
            img = font.render(turn, 1, (255,255,255))
            window.blit(img,list_of_coords[move])
            pygame.display.update()
            turn='X'
        count()
    if len(won)==1:
        text("You lost.", (255, 0, 0))
    else:
        text("You Tied!", (0, 0, 255))
    eventgrabber()

def drawBoard():
    values = [0, 0, 0]
    for c in range(len(values)):
        values[c] = random.randrange(0, 255)
    for n in range(1,3):
        pygame.draw.line(window,values,(200*n,0),(200*n,600),5)
        pygame.draw.line(window,values,(0,200*n),(600,200*n),5)
    pygame.display.update()

    
def flashBorderAnimation(animationSpeed=30):
    time.sleep(1)
    flashSurf = pygame.Surface(window.get_size())
    flashSurf = flashSurf.convert_alpha()
    for start, end, step in ((0, 256, 1), (255, 0, -1)):
        for transparency in range(start, end, animationSpeed * step):
            values = [0, 0, 0, 0]
            for c in range(len(values)):
                values[c] = random.randrange(0, 255)
            flashSurf.fill(values)
            window.blit(flashSurf, (0, 0))
            pygame.display.update()

def text(text, color):
    eventgrabber()
    flashBorderAnimation()
    msg = font.render(text, 1, color)
    window.blit(msg, (600 / 2 - 200, 600 / 2 - 100))
    pygame.display.update()
    time.sleep(1)
    resetBoard()

if __name__=='__main__':
    resetBoard()
    while 1:
        tttai()
