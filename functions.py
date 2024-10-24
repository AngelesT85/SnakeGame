from classes import *

def CreateSnake(field):
    '''
    function create start snake on the (7, 8) (8, 8) (9, 8) coords
    '''
    d = {
        0: "head",
        1: "body",
        2: "tail"
    }
    for row in d:
        snake = Snake(field, (6 + row, 7), (d[row], 0))