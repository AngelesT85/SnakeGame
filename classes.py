from random import randint
from loads.images import Apple, Pear

food = (Apple, Pear)

class Field:
    def __init__(self):
        self.field = [["-" for i in range(15)] for j in range(15)]
    
    def UpdateField(self):
        for segment in Snake.Segments:
            string = segment.coords[0]
            col = segment.coords[1]
            self.field[string][col] = segment

    
    def Print(self, change_snake=True):
        '''
        function print field
        change_snake - will objects of Snake print like 'class.__Snake__...' (change_snake = False)
                                                or
                        objects of Snake will printed like 'o' (change_snake = True (by default))
        '''
        for i in self.field:
            for j in i:
                
                if isinstance(j, Snake):
                    if change_snake:
                        print("o", end=" ")
                    else:
                        print(j, end=" ")

                else:
                    print(j, end=" ")
            print()

class Apple:
    def __init__(self):
        self.image = food[randint(0, 1)]
        
class Snake:
    Segments = list()

    def __init__(self, coords, position):
        '''
        function create new segment of snake (at start of the game and when eat apple)
        coords (tuple) - where on the field will appear segment of snake. (string, column)
        position (tuple) - what kind of piece of snake (head/body/tail) and degree for the picture. ('head'/'body'/'tail', 90)
        '''
        self.status = position[0]
        self.degree = position[1]
        self.coords = coords

        Snake.Segments.append(self)
    
    def Move():
        pass