# automaticly pip install pygame
try:
    import pygame as pg
except:
    from subprocess import check_call
    from sys import executable
    check_call([executable, "-m", "pip", "install", "pygame"])

from loads.images import *

def Snake():
    pg.init()

    screen = pg.display.set_mode((912, 912))
    screen.fill((255, 255, 255))
    screen.blit(FieldImg, (0, 0))
    
    is_game = True

    while is_game:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                is_game = False
        
        pg.display.flip()

Snake()
