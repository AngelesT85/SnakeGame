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
        self.field = [["-" for i in range(15)] for j in range(15)]

        for segment in Snake.Segments:
            string = segment.coords[0]
            col = segment.coords[1]
            self.field[string][col] = segment
        
        self.field[Food.coords[0]][Food.coords[1]] = Food()

    
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
    coords = (0, 0)

    def __init__(self):
        self.image = food[randint(0, 1)]
    
    def Spawn(field):
        '''
        function spawn food (apple or pear) on the field
        field - field for comp (you can watch it if turn it in settings.json)
        '''
        while True:
            string = randint(0, 14)
            col = randint(0, 14)

            if not isinstance(field[string][col], Snake):
                field[string][col] = Food()
                Food.coords = (string, col)
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
        self.position = position
        self.coords = coords
        Snake.Length += 1
        Snake.Segments.append(self)
    
    def Move(field, ChangeCoords, IsTurn, NewDire):
        NewStr = ChangeCoords[0]
        NewCol = ChangeCoords[1]

        FirstSegment = Snake.Segments[0]

        # check move coords
        newstr = NewStr + FirstSegment.coords[0]
        newcol = NewCol + FirstSegment.coords[1]

        if (0 <= newstr <= 14) and (0 <= newcol <= 14):
            if isinstance(field[newstr][newcol], Snake):
                return False, newstr, newcol

        PreLastSegment = Snake.Segments[-2]
        LastSegment = Snake.Segments[-1]

        LastSegment.coords = (FirstSegment.coords[0] + NewStr, FirstSegment.coords[1] + NewCol)
        LastSegment.position[0] = "head"

        # if turn
        if IsTurn:
            Snake.Segments[0].position[0] = "turn"
            LastSegment.position[2] = NewDire
            
            if ChangeCoords in ((1, 0), (0, -1)):
                LastSegment.position[1] += 90
                
            else:
                LastSegment.position[1] -= 90

        # if not turn 
        else:
            Snake.Segments[0].position[0] = "body"
            LastSegment.position[1] = FirstSegment.position[1]
        
        PreLastSegment.position[0] = "tail"

        if Snake.Segments[-3].position[0] == "turn":
            PreLastSegment.position[1] = Snake.Segments[-3].position[1] - 90

        else:
            PreLastSegment.position[1] = Snake.Segments[-3].position[1]
        
        del Snake.Segments[-1]
        Snake.Segments.insert(0, LastSegment)

        return True
            
