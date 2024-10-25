# automaticly pip install pygame
try:
    import pygame as pg
except:
    from subprocess import check_call
    from sys import executable
    check_call([executable, "-m", "pip", "install", "pygame"])

from loads.images import *
from functions import *
from classes import *

def Snake():
    pg.init()

    field = Field()

    CreateSnake()
    field.UpdateField()

    field.Print()

    screen = pg.display.set_mode((912, 912))
    screen.fill((255, 255, 255))
    screen.blit(FieldImg, (0, 0))
    screen.blit(Start, (0, 0))

    
    is_game = True

    while is_game:
        DrawSnake(screen, field.field)
        DrawFood(screen, field.field)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                is_game = False
            
            elif event.type == pg.MOUSEBUTTONDOWN:
                x, y = pg.mouse.get_pos()
                if (217 <= x <= 696) and (0 <= y <= 123):
                    food = Food()
                    food.Spawn(field.field)
                    print(1)

        
        pg.display.flip()

Snake()
