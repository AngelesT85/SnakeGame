from random import randint
from loads.images import Apple, Pear

food = (Apple, Pear)

class Field:
    def __init__(self):
        self.field = [["-" for i in range(15)] for j in range(15)]
    
    def UpdateField(self) -> None:
        '''
        function update field after snake move
        '''
        for segment in Snake.Segments:
            string = segment.coords[0]
            col = segment.coords[1]
            self.field[string][col] = segment

    
    def Print(self, change_snake = True, change_food = True) -> None:
        '''
        function print field
        change_snake - will objects of Snake print like 'class.__Snake__...' (change_snake = False)
                                                or
                        objects of Snake will printed like 'o' (change_snake = True (by default))

        change_food - will objects of Food print like 'class.__Food__...' (change_food = False)
                                                or
                        objects of Food will print like 'f' (change_food = True (by default))
        '''
        for i in self.field:
            for j in i:
                
                # print snake segment
                if isinstance(j, Snake):
                    if change_snake:
                        print("o", end=" ")
                    else:
                        print(j, end=" ")
                
                # print food
                elif isinstance(j, Food):
                    if change_food:
                        print("f", end=" ")
                    else:
                        print(j, end=" ")

                else:
                    print(j, end=" ")

            print()

class Food:
    def __init__(self):
        self.image = food[randint(0, 1)]
    
    def Spawn(self, field):
        '''
        function spawn food (apple or pear) on the field
        field - field for comp (you can watch it if turn it in settings.json)
        '''
        while True:
            string = randint(0, 14)
            col = randint(0, 14)

            if not isinstance(field[string][col], Snake):
                field[string][col] = self
                break

class Snake:
    Segments = list()
    Length = 0

    def __init__(self, coords, position):
        '''
        function create new segment of snake (at start of the game and when eat apple)
        coords (tuple) - where on the field will appear segment of snake. (string, column)
        position (tuple) - what kind of piece of snake ('head'/'body'/'tail'/'turn'), 
                           angle (degree) for the picture and direction of segment ('left'/'up'/'down'/'right'). (piece_of_snake, angle, direction)
        '''
        self.status = position[0]
        self.degree = position[1]
        self.direction = position[2]
        self.coords = coords
        Snake.Length += 1

        Snake.Segments.append(self)
    
    def Move(field, ChangeCoords, IsTurn, NewDire):
        NewStr = ChangeCoords[0]
        NewCol = ChangeCoords[1]

        FirstSegment = Snake.Segments[0]
        LastSegment = Snake.Segments.pop(-1)

        LastSegment.coords = (FirstSegment.coords[0] + NewStr, FirstSegment.coords[1] + NewCol)
        LastSegment.position[0] = "head"
        LastSegment.position[2] = NewDire 

        if IsTurn:
            Snake.Segments[0].position[0] = "turn"

            if ChangeCoords in ((1, 0), (0, -1)):
                FirstSegment.position[1] = FirstSegment.position[1]

        

        pass