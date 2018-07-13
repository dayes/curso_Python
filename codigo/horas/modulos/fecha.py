# clase Fecha

class Fecha:
	
	def __init__(self, d=1,m=1,y=1970):
		self.d = d
		self.M = m
		self.y = y
		
	def __str__(self):
		return str("%02d/%02d/%d" % (self.d,self.M,self.y))
		
	def __repr__(self):
		return str("%02d/%02d/%d" % (self.d,self.M,self.y))
