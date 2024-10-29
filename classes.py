from random import randint
from loads.images import Apple, Pear
from dicks import * 

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
        
        Food.Spawn(self.field)
    
    def Print(self, change_snake = True, change_food = True) -> None:
        '''
        function print field
        change_snake - will objects of Snake print like 'classes.Snake...' (change_snake = False)
                                                or
                        objects of Snake will printed like 'o' (change_snake = True (by default))

        change_food - will objects of Food print like 'classes.Food...' (change_food = False)
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
    
    def Spawn(field):
        '''
        function spawn food (apple or pear) on the field
        field - field for comp (you can watch it if turn it in settings.json)
        '''
        while True:
            string = randint(0, 14)
            col = randint(0, 14)

            if not isinstance(field[string][col], Snake) or not not isinstance(field[string][col], Food):
                field[string][col] = Food()
                Food.coords = (string, col)
                Snake.Number_food += 1
                break

class Snake:
    Segments = list()
    Length = 0
    Number_food = 0

    def __init__(self, coords, position):
        '''
        function create new segment of snake (at start of the game and when eat apple)
        coords (tuple) - where on the field will appear segment of snake. (string, column)
        position (tuple) - what kind of piece of snake ('head'/'body'/'tail'/'turn') 
                           and direction of segment ('left'/'up'/'down'/'right'). (piece_of_snake, angle, direction)
        '''
        self.position = position
        self.coords = coords
        Snake.Length += 1
        Snake.Segments.append(self)
    
    def Move(Field, Dire):
        field = Field.field
        NewStr = Dires[Dire][1][0]
        NewCol = Dires[Dire][1][1]

        FirstSegment = Snake.Segments[0]

        # check move coords
        newstr = NewStr + FirstSegment.coords[0]
        newcol = NewCol + FirstSegment.coords[1]
        if (newstr < 0 or newstr > 14) or (newcol < 0 or newcol > 14) or isinstance(field[newstr][newcol], Snake):
            return False, "die"
        
        # eat food
        elif isinstance(field[newstr][newcol], Food):
            if FirstSegment.position[1] == Dire:
                s = Snake([newstr, newcol], ["head", FirstSegment.position[1]])
                LastSegment = Snake.Segments.pop(-1)
                Snake.Segments.insert(0, LastSegment)
                FirstSegment.position[0] = "body"
                Snake.Number_food -= 1
                Field.UpdateField()
                Food.Spawn(field)
            
                return True, "eat"
            else:
                

        # just move
        else:    
            PreLastSegment = Snake.Segments[-2]
            LastSegment = Snake.Segments[-1]

            LastSegment.position[0] = "head"
            LastSegment.position[1] = Dire
            LastSegment.coords = (newstr, newcol)

            PreLastSegment.position[0] = "tail"
            PreLastSegment.position[1] = Snake.Segments[-3].position[1]
            
            # not turn
            if Dire == FirstSegment.position[1]:

                FirstSegment.position[0] = "body"
            
            # snake turn
            else:
                FirstSegment.position[0] =  "turn"
                LastSegmentDire = LastSegment.position[1]
                FirstSegmentDire = FirstSegment.position[1]
                
                TuplesSum = Dires[LastSegmentDire][1] + Dires[FirstSegmentDire][1]

                # i dont know how it works but it works
                if len(set(TuplesSum)) == 2:
                    if sorted(tuple(set(TuplesSum)))[0] == 0:
                        FirstSegment.position[1] = Antonims[FirstSegment.position[1]]
                    else:
                        FirstSegment.position[1] = Dire
                
                elif len(set(TuplesSum)) == 3:
                    FirstSegment.position[1] = Antonims[FirstSegment.position[1]]

        Snake.Segments[0] = FirstSegment
        Snake.Segments[-2] = PreLastSegment

        del Snake.Segments[-1]
        Snake.Segments.insert(0, LastSegment)
        
        return True, "move"
            
