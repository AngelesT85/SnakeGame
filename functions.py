from classes import *
from loads.images import *
from pygame.transform import rotate

def CreateSnake():
    '''
    function create start snake on the (7, 8) (8, 8) (9, 8) coords
    '''
    d = {
        0: "head",
        1: "body",
        2: "tail"
    }
    for row in d:
        snake = Snake([6 + row, 7], [d[row], 0, "up"])

def DrawSnake(screen, field, head, body, turn, tail):
    for part_snake in Snake.Segments:

        status = part_snake.position[0]
        x, y = part_snake.coords[1], part_snake.coords[0]
        RotationAngle = part_snake.position[1]

        global SnakeHead, SnakeBody, SnakeTurn, SnakeTail

        if status == "head":
            SnakeHead = rotate(head, RotationAngle)
            screen.blit(head, (96 + 48 * x, 160 + 48 * y))

        elif status == "body":
            SnakeBody = rotate(body, RotationAngle)
            screen.blit(body, (96 + 48 * x, 160 + 48 * y))

        elif status == "tail":
            SnakeTail = rotate(tail, RotationAngle)
            screen.blit(tail, (96 + 48 * x, 160 + 48 * y))
        
        elif status == "turn":
            SnakeTurn = rotate(turn, RotationAngle)
            screen.blit(turn, (96 + 48 * x, 160 + 48 * y))
            

def DrawFood(screen, field):
    for i in range(15):
        for j in range(15):
            if type(field[i][j]) == Food:
                screen.blit(field[i][j].image, (96 + 48 * j, 160 + 48 * i))


    