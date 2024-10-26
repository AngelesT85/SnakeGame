from classes import *
from loads.images import *

def CreateSnake():
    '''
    function create start snake on the (7, 8) (8, 8) (9, 8) coords
    '''
    d = {
        2: "head",
        1: "body",
        0: "tail"
    }
    for row in d:
        snake = Snake([6 + row, 7], [d[row], 0, "up"])

def DrawSnake(screen, field):
    for part_snake in Snake.Segments:
        if part_snake.position[0] == "head":
            screen.blit(SnakeHead, (96 + 48 * part_snake.coords[1], 160 + 48 * part_snake.coords[0]))
        elif part_snake.position[0] == "body":
            screen.blit(SnakeBody, (96 + 48 * part_snake.coords[1], 160 + 48 * part_snake.coords[0]))
        elif part_snake.position[0] == "tail":
            screen.blit(SnakeTail, (96 + 48 * part_snake.coords[1], 160 + 48 * part_snake.coords[0]))

def DrawFood(screen, field):
    for i in range(15):
        for j in range(15):
            if type(field[i][j]) == Food:
                screen.blit(field[i][j].image, (96 + 48 * j, 160 + 48 * i))


    