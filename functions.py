from classes import *
from loads.images import *
from pygame.transform import rotate
from dicks import Dires

def CreateSnake():
    '''
    function create start snake on the (7, 8) (8, 8) (9, 8) coords
    '''
    d = {
        0: "head",
        1: "body",
        2: "tail"
    }
    Snake.Segments.clear()
    for row in d:
        s = Snake([6 + row, 7], [d[row], "up"])

def DrawSnake(screen):
    for part_snake in Snake.Segments:

        status = part_snake.position[0]
        x, y = part_snake.coords[1], part_snake.coords[0]
        RotationAngle = Dires[part_snake.position[1]][0]

        if status == "head":
            h = SnakeHead
            head = rotate(h, RotationAngle)
            screen.blit(head, (96 + 48 * x, 160 + 48 * y))

        elif status == "body":
            b = SnakeBody
            body = rotate(b, RotationAngle)
            screen.blit(body, (96 + 48 * x, 160 + 48 * y))

        elif status == "tail":
            ta = SnakeTail
            tail = rotate(ta, RotationAngle)
            screen.blit(tail, (96 + 48 * x, 160 + 48 * y))
        
        elif status == "turn":
            tu = SnakeTurn
            turn = rotate(tu, RotationAngle)
            screen.blit(turn, (96 + 48 * x, 160 + 48 * y))
            

def DrawFood(screen, field):
    for i in range(15):
        for j in range(15):
            if type(field[i][j]) == Food:
                screen.blit(field[i][j].image, (96 + 48 * j, 160 + 48 * i))


    