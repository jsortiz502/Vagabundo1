import random

class Homeless:
    
	def __init__(self, name):
		self.name = name
  		self.x = x
    	self.y = y
  
	def posicion(self):
		return(self.x, self.y)

	def distance_origin(self):
    	return(self.x**2 + self.y**2)**0.5

class StandarHomeless(Homeless):
	def __init__(self, name):
		super().__init__(name)

	def walk(self):
		return random.choice([(0,1), (-1,0), (0,1), (0,-1)])

