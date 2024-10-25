from functions import *

field = Field()

food = Food()
food.Spawn(field.field)

CreateSnake()
field.UpdateField()

field.Print()

