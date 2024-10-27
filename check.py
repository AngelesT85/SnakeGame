from functions import *

field = Field()

Food.Spawn(field.field)

CreateSnake()
field.UpdateField()

print(Snake.Segments)

result = Snake.Move(field.field, (-1, 0), False, "d")
result = Snake.Move(field.field, (0, 1), True, "right")
# result = Snake.Move(field.field, (-1, 0), False, "d")
field.UpdateField()

for segment in Snake.Segments:
    print(segment.position[0])

print(Snake.Segments)
print(result)
field.Print()
