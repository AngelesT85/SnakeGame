from pygame.image import load

def Load(image):
    return load(f"images/{image}.png")

FieldImg = Load("field")
Pear = Load("pear")
SnakeTail = Load("snake end")
SnakeBody = Load("snake middle")
SnakeHead = Load("snake head")
<<<<<<< HEAD
Apple = Load("apple")
Start = Load("start")
=======
SnakeTurn = Load("body turn")
Apple = Load("apple")
>>>>>>> 78f36b8cb19ce09bd5f8b2c10c40b7ebbb199835
