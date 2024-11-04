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
Win = Load("win")

Zero = Load("zero")
One = Load("one")
Two = Load("two")
Three = Load("three")
Four = Load("four")
Five = Load("five")
Six = Load("six")
Seven = Load("seven")
Eight = Load("eight")
Nine = Load("nine")