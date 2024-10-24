class Field:
    def __init__(self):
        self.field = [["-" for i in range(15)] for j in range(15)]
    
    def Print(self, change_snake=True):
        '''
function print field
change_snake - will objects of Snake print like 'class.__Snake__...' (change_snake = False)
                                        or
                objects of Snake will printed like 'o'
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


class Snake:
    Segments = list()

    def __init__(self, field, coords, position):
        '''
function create new segment of snake (at start of the game and when eat apple)
field (matrix) - field on which snake is crawl.
coords (tuple) - where on the field will appear segment of snake. (string, column)
position (tuple) - what kind of piece of snake (head/body/tail) and degree for the picture. (head/body/tail, 90)
        '''
        self.status = position[0]
        self.degree = position[1]
        self.coords = coords

        string = coords[0]
        col = coords[1]
        field[string][col] = self
