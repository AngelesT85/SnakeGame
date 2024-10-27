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

def snake():
    pg.init()

    field = Field()

    CreateSnake()
    field.UpdateField()

    field.Print()

    
    result = Snake.Move(field.field, (0, 1), True, "right")
    # result = Snake.Move(field.field, (-1, 0), False, "d")
    field.UpdateField()

    for segment in Snake.Segments:
        print(segment.position[0])

    print(Snake.Segments)
    print(result)
    field.Print()

    screen = pg.display.set_mode((912, 912))
    screen.fill((255, 255, 255))
    screen.blit(FieldImg, (0, 0))


    
    is_game = True
    game_start = False

    DrawSnake(screen, field.field)

    while is_game:
        if game_start:
            Food.Spawn(field.field)
            screen.blit(Restart, (0, 0))
        else:
            screen.blit(Start, (0, 0))

        # DrawSnake(screen, field.field)
        DrawFood(screen, field.field)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                is_game = False
            
            elif event.type == pg.MOUSEBUTTONDOWN:
                x, y = pg.mouse.get_pos()
                if (217 <= x <= 696) and (0 <= y <= 123):
                    if game_start == False:
                        game_start = True
                    else:
                        game_start = False

                        screen.blit(FieldImg, (0, 0))
                        field = Field()
                        CreateSnake()
                        field.UpdateField()
                
            elif event.type == pg.K_LEFT:
                DrawSnake(screen, field.field)



        
        pg.display.flip()

snake()
