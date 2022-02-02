class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def move(self, delta_x, delta_y):
        return Coordinate(self.x, + delta_x, self.y + delta_y)
    
    def distance(self, other, coordinate):
        delta_x = self.x - otra_coordenada.x
        delta_y = self.y - otra_coordenada.y
        
        return(delta_x**2 + delta_y**2)**0.5