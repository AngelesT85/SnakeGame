from functions import *

field = Field()

food = Food()
food.Spawn(field.field)

CreateSnake()
field.UpdateField()

result = Snake.Move(field.field, (1, 0), False, "d")
field.UpdateField()

print(result)
field.Print()
