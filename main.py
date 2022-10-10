import pygame as pg

NUMBER_OF_ROWS = 20
NUMBER_OF_COLUMNS = 20
NUMBER_TO_WIN = 5
FPS = 144
SIZE_OF_SINGLE_BOX = 60

board2d = t = [[-1] * NUMBER_OF_COLUMNS for i in range(NUMBER_OF_ROWS)]

BACKGROUND = (23, 29, 62)
BACKGROUND_PANEL = (171, 209, 229)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (204, 0, 0)
YELLOW = (255, 255, 153)
BLUE = (77, 77, 255)
GREEN = (0, 255, 0)
PURPLE = (255, 0, 255)
SKY = (0, 255, 255)
ORANGE = (255, 125, 25)
GRAPE = (100, 25, 125)
GRASS = (55, 155, 65)
PINK = (204, 0, 102)

dimension = (NUMBER_OF_COLUMNS * SIZE_OF_SINGLE_BOX + 20, NUMBER_OF_ROWS * SIZE_OF_SINGLE_BOX + 50)

# initialize all imported pygame modules
pg.init()
# Set dimension
screen = pg.display.set_mode(dimension)
# Set Caption
pg.display.set_caption("kmeans visualization")

running = True
clock = pg.time.Clock()


def drawPanel():
    pg.draw.rect(screen, BLACK, (8, 38, dimension[0] - 16, dimension[1] - 46))


def drawMarks():
    originBoard = (10 + SIZE_OF_SINGLE_BOX / 5, 40)
    for i in range(len(board2d)):
        for j in range(len(board2d[i])):
            if check_value(board2d[i][j]) == " X ":
                screen.blit(render_mark("X", SIZE_OF_SINGLE_BOX - 3),
                            (originBoard[0] + j * SIZE_OF_SINGLE_BOX, originBoard[1] + i * SIZE_OF_SINGLE_BOX))
            elif check_value(board2d[i][j]) == " O ":
                screen.blit(render_mark("O", SIZE_OF_SINGLE_BOX - 3),
                            (originBoard[0] + j * SIZE_OF_SINGLE_BOX, originBoard[1] + i * SIZE_OF_SINGLE_BOX))
            else:
                screen.blit(render_mark(" ", SIZE_OF_SINGLE_BOX - 3),
                            (originBoard[0] + j * SIZE_OF_SINGLE_BOX, originBoard[1] + i * SIZE_OF_SINGLE_BOX))


def check_value(x):
    if x == -1:
        return "   "
    elif x == 0:
        return " O "
    else:
        return " X "


def render_mark(string, size):
    font = pg.font.SysFont('dejavuserif', size)
    if string == "X":
        return font.render(string, True, RED)
    elif string == "O":
        return font.render(string, True, BLUE)
    else:
        return font.render(string, True, BLUE)


def render_winner(string, size, colorIndex):
    font = pg.font.SysFont('AniMeMatrix-MB_EN', size)
    if colorIndex == 0:
        return font.render(string, True, BLUE)
    else:
        return font.render(string, True, RED)


def render_border_winner(string, size):
    font = pg.font.SysFont('AniMeMatrix-MB_EN', size)
    return font.render(string, True, BLACK)


def drawGrid():
    for i in range(NUMBER_OF_ROWS):
        for j in range(NUMBER_OF_COLUMNS):
            pg.draw.rect(screen, BACKGROUND_PANEL, (
                11 + SIZE_OF_SINGLE_BOX * j, 41 + SIZE_OF_SINGLE_BOX * i, SIZE_OF_SINGLE_BOX - 1,
                SIZE_OF_SINGLE_BOX - 1))


def markingWithPlayer(player, x, y):
    global playerChoose
    if board2d[x][y] == -1:
        if playerChoose == 0:
            board2d[x][y] = 0
        else:
            board2d[x][y] = 1
        if playerChoose == 0:
            playerChoose = 1
        else:
            playerChoose = 0
    else:
        pass


def check_availability(x):
    if x == -1:
        return True
    else:
        return False


def printWinner(winnerSign):
    global gotWinner
    global playing
    global winner
    playing = False
    gotWinner = True
    pg.draw.rect(screen, YELLOW,
                 (0, int(dimension[1] / 3) + 5, dimension[0], int(dimension[0] * dimension[1] / 15000) + 3))
    if (winnerSign == 0):
        winner = 0
        screen.blit(render_border_winner("PLAYER 1 WON!", int(dimension[0] * dimension[1] / 15000)),
                    (int(dimension[0] / 11) + 2, int(dimension[1] / 3) - 2))
        screen.blit(render_winner("PLAYER 1 WON!", int(dimension[0] * dimension[1] / 15000), 0),
                    (int(dimension[0] / 11), int(dimension[1] / 3)))
    else:
        winner = 1
        screen.blit(render_border_winner("PLAYER 2 WON!", int(dimension[0] * dimension[1] / 15000)),
                    (int(dimension[0] / 12) + 3, int(dimension[1] / 3) - 2))
        screen.blit(render_winner("PLAYER 2 WON!", int(dimension[0] * dimension[1] / 15000), 1),
                    (int(dimension[0] / 12), int(dimension[1] / 3)))


def winner_checker():
    # check diagonal left
    for i in range(0, NUMBER_OF_ROWS - NUMBER_TO_WIN + 1):
        if gotWinner == False:
            for j in range(0, NUMBER_OF_COLUMNS - NUMBER_TO_WIN + 1):
                if gotWinner == False:
                    if check_availability(board2d[i][j]) == False:
                        counter = 0
                        temp_y = i
                        temp_x = j
                        for g in range(0, NUMBER_TO_WIN - 1):
                            if (board2d[temp_y][temp_x] == board2d[temp_y + 1][temp_x + 1]):
                                temp_y += 1
                                temp_x += 1
                                counter += 1
                                if (counter >= NUMBER_TO_WIN - 1):
                                    printWinner(board2d[i][j])
                                    break
                            else:
                                break
                else:
                    break
        else:
            break
    # check diagonal right
    for i in range(0, NUMBER_OF_ROWS - NUMBER_TO_WIN + 1):
        if gotWinner == False:
            for j in range(NUMBER_TO_WIN - 1, NUMBER_OF_COLUMNS):
                if gotWinner == False:
                    if check_availability(board2d[i][j]) == False:
                        temp_y = i
                        temp_x = j
                        counter = 0
                        for g in range(0, NUMBER_TO_WIN - 1):
                            if (board2d[temp_y][temp_x] == board2d[temp_y + 1][temp_x - 1]):
                                temp_y += 1
                                temp_x -= 1
                                counter += 1
                                if (counter >= NUMBER_TO_WIN - 1):
                                    printWinner(board2d[i][j])
                                    break
                            else:
                                break
                else:
                    break
        else:
            break
    # check vertical line
    for i in range(0, NUMBER_OF_ROWS - NUMBER_TO_WIN + 1):
        if gotWinner == False:
            for j in range(0, NUMBER_OF_COLUMNS):
                if gotWinner == False:
                    if check_availability(board2d[i][j]) == False:
                        temp_y = i
                        temp_x = j
                        counter = 0
                        for g in range(0, NUMBER_TO_WIN - 1):
                            if (board2d[temp_y][temp_x] == board2d[temp_y + 1][temp_x]):
                                temp_y += 1
                                counter += 1
                                if (counter >= NUMBER_TO_WIN - 1):
                                    printWinner(board2d[i][j])
                                    break
                            else:
                                break
                else:
                    break
        else:
            break
    # check horizontal line
    for i in range(0, NUMBER_OF_ROWS):
        if gotWinner == False:
            for j in range(0, NUMBER_OF_COLUMNS - NUMBER_TO_WIN + 1):
                if gotWinner == False:
                    if check_availability(board2d[i][j]) == False:
                        temp_y = i
                        temp_x = j
                        counter = 0
                        for g in range(0, NUMBER_TO_WIN - 1):
                            if (board2d[temp_y][temp_x] == board2d[temp_y][temp_x + 1]):
                                temp_x += 1
                                counter += 1
                                if (counter >= NUMBER_TO_WIN - 1):
                                    printWinner(board2d[i][j])
                                    break
                            else:
                                break
                else:
                    break
        else:
            break


playerChoose = 0
gotWinner = False
playing = True
winner = -1

while running:
    mouse_x, mouse_y = pg.mouse.get_pos()
    # Set FPS
    clock.tick(FPS)
    screen.fill(BACKGROUND)
    drawPanel()
    drawGrid()
    drawMarks()
    if playing == True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                # print(str(mouse_x) + ", " + str(mouse_y))
                if 10 < mouse_x < dimension[0] - 10 and 40 < mouse_y < dimension[1] - 10:
                    clickedX = int((mouse_x - 10) / SIZE_OF_SINGLE_BOX)
                    clickedY = int((mouse_y - 40) / SIZE_OF_SINGLE_BOX)
                    # print("X: " + str(clickedX))
                    # print("Y: " + str(clickedY))
                    # print("======")
                    markingWithPlayer(playerChoose, clickedY, clickedX)
                    winner_checker()
    else:
        printWinner(winner)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
    pg.display.flip()
pg.quit()
