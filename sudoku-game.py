import pygame
import numpy as np
from solve import solve1
import time

pygame.init()

pygame.display.set_caption("Sudoku")
clock = pygame.time.Clock()


blue = pygame.Color("blue")
white = pygame.Color("white")
black = pygame.Color("black")
hwhite = (220, 220, 220)
ch_color = (100, 20, 10)
ch_color1 = (180, 10, 10)
solu_color = (10, 110, 20)
solu_color1 = (10, 180, 20)

sq_height = 98
sq_width = 98
sq_x = 6
sq_y = 6

WIDTH = 919
HEIGHT = 1060

screen = pygame.display.set_mode((WIDTH, HEIGHT))


point = [()]

font = pygame.font.Font(None, 70)
font2 = pygame.font.Font('freesansbold.ttf', 32)
fnt = pygame.font.SysFont("comicsans", 55)
square_list = []
arg_list = [''] * 81
n = ''
active = False
sq_index = ''
sq_index2 = None

template1 = ['4', '', '', '', '9', '', '', '', '', '', '1', '', '', '', '', '3', '', '', '', '8', '', '', '', '', '1',
             '', '7', '', '', '6', '', '', '', '', '', '3', '', '', '9', '', '7', '2', '', '5', '', '', '', '', '', '',
             '4', '', '2', '6', '', '', '2', '', '', '7', '', '8', '', '5', '', '', '', '', '6', '', '', '', '', '', '',
             '8', '5', '', '', '', '']




for k in range(9):
    for y in range(3):
        for i in range(3):
            # pygame.draw.rect(screen, hwhite, pygame.Rect((sq_x, sq_y), (sq_width, sq_height)))
            square_list.append(pygame.Rect((sq_x, sq_y), (sq_width, sq_height)))
            sq_x += (2 + sq_width)
        sq_x += 3
    sq_x = 6
    if k == 2 or k == 5:
        sq_y += (5 + sq_height)
    else:
        sq_y += (2 + sq_height)

grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]

gridans = [['', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '', '']]

ans_grid = []


def possibleAns(y, x, n):
    global grid
    for i in range(0,9):
        if grid[y][i] ==n:
            return False
    for i in range(0,9):
        if grid[i][x]==n :
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j] == n:
                return False
    return True


def solve(ar):
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if possibleAns(y, x, n):
                        grid[y][x] = n
                        solve(ar)
                        grid[y][x] = 0
                return
    print(np.matrix(grid))
    filingd(grid, ar)


def filing(lst):
    global grid
    a = 0
    for r in range(9):
        for c in range(9):
            if lst[a] != '':
                grid[r][c] = int(lst[a])
            a += 1


def filingd(g, ar):
    a = 0
    for r in range(9):
        for c in range(9):
            if ar[a] != '':
                ar[a] = str(g[r][c])



def isOver(self, pos):
    # Pos is the mouse position or a tuple of (x,y) coordinates
    if self.x < pos[0] < self.x + self.width:
        if self.y < pos[1] < self.y + self.height:
            return True

def correct_ans(sqlst, anslist):
    anslist = [str(sqlst) for sq in sqlst]
    for i, v in zip(sqlst, anslist):
        screen.blit(font.render(v, True, (255, 0, 0)), (i.x + 34, i.y + 31))


def tostringL(listt):
    g = [['' for i in range(9)] for j in range(9)]

    for i in range(9):
        for j in range(9):
            g[i][j] = str(listt[i][j])


    return g

def tostringL1d(listt):
    g = [''] * 81


    for i in range(81):
        if listt[i] != 0:
            g[i] = str(listt[i])
        else:
            g[i] = ''

    return g


def encoding(lst):
    l = []
    for i in range(9):
        for j in range(9):
            l.append(bytes(lst[i][j], 'ascii'))
    return l

def encoding1d(lst):
    l = []
    for i in range(81):

        l.append(bytes(lst[i], 'ascii'))
    return l

def printen(sq, val, t):
    if t == 1:
        screen.blit(font.render(val, True, (255, 0, 0)), (sq.x + 34, sq.y + 31))
    else:
        screen.blit(font2.render(val, True, hwhite), (sq.x + 13, sq.y + 16))


def printsolve(arg_list, grid):
    filing(arg_list, grid)
    print("111", grid)
    # solve(arg_list)
    return solve1(grid)

def time1(secs):
    sec = secs%60
    minute = secs//60
    hour = minute//60

    mat = " " + str(minute) + ":" + str(sec)
    return mat

# ch = 'CHECK'
solv = 'SOLVE'
check_box = pygame.Rect((300, HEIGHT - 97), (140, 60))
solve_box = pygame.Rect((530, HEIGHT - 97), (140, 60))

timerOn = True

print(template1, "-> ", len(template1))
template1a = encoding1d(template1)
print(template1, "-> ", len(template1))
text = font.render('GeeksForGeeks', True, white, blue)
start = time.time()
run = True
while run:

    play_time = round(time.time() - start)
    if timerOn : text = fnt.render("Time: " + time1(play_time), 1, (0, 255, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                arg_list[sq_index] = arg_list[sq_index][:-1]
            if len(arg_list[sq_index]) < 1:
                if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6,
                                 pygame.K_7, pygame.K_8, pygame.K_9]:
                    arg_list[sq_index] += event.unicode



        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in square_list:
                if isOver(i, event.pos) and template1a[square_list.index(i)] == b'':
                    active = True
                    sq_index = square_list.index(i)

            if isOver(solve_box, event.pos):
                filing(template1)
                filing(arg_list)
                # print("this is grid --- ", grid)
                # print("this is arg --- ", arg_list)
                # solve(arg_list)
                grid = solve1(grid)
                print(grid)
                # correct_ans(square_list,ngrid)

                gridans = tostringL(grid)
                print(gridans)
                enc = encoding(gridans)
                print(enc)
                arg_list = enc.copy()
                timerOn = False




    screen.fill((0, 0, 0))
    screen.blit(text, (720, 970))
    e = pygame.mouse.get_pos()

    # if isOver(check_box, e):
    #     pygame.draw.rect(screen, ch_color1, check_box)
    # else:
    #     pygame.draw.rect(screen, ch_color, check_box)
    # printen(check_box, ch, 2)

    if isOver(solve_box, e):
        pygame.draw.rect(screen, solu_color1, solve_box)
    else:
        pygame.draw.rect(screen, solu_color, solve_box)
    printen(solve_box, solv, 2)


    for i in range(81):
        if isOver(square_list[i], e):
            pygame.draw.rect(screen, hwhite, square_list[i])
        else:
            pygame.draw.rect(screen, white, square_list[i])
        printen(square_list[i], arg_list[i], 1)
        printen(square_list[i], template1a[i], 1)
        if active:
            pygame.draw.rect(screen, hwhite, square_list[sq_index])
            printen(square_list[sq_index], arg_list[sq_index], 1)

    pygame.display.flip()

pygame.quit()
quit()
