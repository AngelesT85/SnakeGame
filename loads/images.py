from pygame.image import load

def Load(image):
    return load(f"images/{image}.png")

FieldImg = Load("field")

Apple = Load("apple")
Pear = Load("pear")

SnakeTail = Load("snake end")
SnakeBody = Load("snake middle")
SnakeHead = Load("snake head")
SnakeTurn = Load("body turn")

Start = Load("start")
Restart = Load("restart")

Lose = Load("lose")

Zero = Load("zero")
One = Load("one")
Two = Load("two")