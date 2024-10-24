from classes import *

def CreateSnake(field):
    '''
    function create start snake on the (7, 8) (8, 8) (9, 8) coords
    '''
    for status, row in ("head", "body", "tail"), range(3):
        snake = Snake(field, (7 + row, 8), (status, 0))