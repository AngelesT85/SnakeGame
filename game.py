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
from loads.settings import *
from dicks import *

def snake():
    pg.init()

    field = Field()

    CreateSnake()
    field.UpdateField()

    #field.Print()
    
    #result = Snake.Move(field.field, "up")
    
    #field.UpdateField()

    #for segment in Snake.Segments:
    #    print(segment.position[0])

    #print(Snake.Segments[1].position)
    #print(result)
    #field.Print()

    screen = pg.display.set_mode((912, 912))
    screen.fill((255, 255, 255))
    screen.blit(FieldImg, (0, 0))
    
    is_game = True
    game_start = False
    lost = False
    count = 0


    while is_game:
        # if count > 15:
        #     print(count)

        screen.blit(FieldImg, (0, 0))
        if game_start:
            screen.blit(Restart, (0, 0))

            # count += 1
            # if count == 25:
            #     count = 0 

                # snake_direction = Snake.Segments[0].position[-1]
                # end_move = Snake.Move(field, snake_direction)
                # field.UpdateField()
                    
                # if not end_move[0] and end_move[1] == "die":
                #     lost = True

                # if PrintConsoleField:
                #     print()
                #     print()
                #     print()
                #     field.Print()


            if Snake.Length == 225:
                print("need doing code about winning")
            
            elif lost:
                screen.blit(Lose, (240, 400))
                score = str(Snake.Length - 3)
                for i in range(len(score)):
                    screen.blit(digits[score[i]], (508 + 4 * (1 + 11 * i), 536))

            elif Snake.Number_food <= 100:
                chance = randint(1, 1000)

                if chance in (250, 750):
                    Food.Spawn(field.field)
                    Snake.Number_food += 1
        else:
            screen.blit(Start, (0, 0))
        DrawSnake(screen)
        DrawFood(screen, field.field)

            
        for event in pg.event.get():
            if event.type == pg.QUIT:
                is_game = False
            
            if event.type == pg.MOUSEBUTTONDOWN:
                x, y = pg.mouse.get_pos()
                if (217 <= x <= 696) and (0 <= y <= 123):
                    if game_start == False:
                        game_start = True
                    else:
                        game_start = False

                        screen.blit(FieldImg, (0, 0))
                        field = Field()
                        field.UpdateField()
                        CreateSnake()
                        DrawSnake(screen)
                        lost = False
            
            elif event.type == pg.KEYDOWN:
                if game_start:
                    if event.key == pg.K_r:
                        game_start = False
                else:
                    if event.key == pg.K_g:
                        game_start = True

            if game_start and not lost:
                if event.type == pg.KEYDOWN:
                    snake_direction = Snake.Segments[0].position[-1]
                    if event.key in (pg.K_LEFT, pg.K_a) and snake_direction != "right":
                        end_move = Snake.Move(field, "left")
                    elif event.key in (pg.K_RIGHT, pg.K_d) and snake_direction != "left":
                        end_move = Snake.Move(field, "right")
                    elif event.key in (pg.K_UP, pg.K_w) and snake_direction != "down":
                        end_move = Snake.Move(field, "up")
                    elif event.key in (pg.K_DOWN, pg.K_s) and snake_direction != "up":
                        end_move = Snake.Move(field, "down")
                    else:
                        end_move = (True, "None")
                    print(end_move)
                    field.UpdateField()
                    if not end_move[0] and end_move[1] == "die":
                        lost = True

                    if PrintConsoleField:
                        field.Print()
        
        pg.display.flip()

snake()
