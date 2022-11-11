import numpy as np

class City():
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name;

    def __str__(self):
        return "City: {0} Coords: {1} {2}\n".format(self.name, self.x, self.y) 

    def distance(self, city):
        xDis = abs(self.x - city.x)
        yDis = abs(self.y - city.y)
        distance = np.sqrt((xDis ** 2) + (yDis ** 2))
        return distance
    
    def __repr__(self):
        return str(self)