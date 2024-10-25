from pygame.image import load

def Load(image):
    return load(f"images/{image}.png")

FieldImg = Load("field")
Pear = Load("pear")
SnakeTail = Load("snake end")
SnakeBody = Load("snake middle")
SnakeHead = Load("snake head")
Apple = Load("apple")
Start = Load("start")