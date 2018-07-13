class Hora:
	
	def __init__(self,h=0,m=0,s=0):
		self.h=h
		self.m=m
		self.s=s
		
	def __str__(self):
		return str("%02d:%02d:%02d" % (self.h,self.m,self.s))

	def __repr__(self):
		return str("%02d:%02d:%02d" % (self.h,self.m,self.s))
		
	def segundos(self):
		return self.h*3600+self.m*60+self.s
		
	def __lt__(self, otro):
		return self.segundos() < otro.segundos()
		
	def __add__(self,otro):
		ss = self.s + otro.s
		mm = (self.m + otro.m) + (ss // 60)
		ss %= 60
		hh = (self.h + otro.h) + (mm // 60)
		mm %= 60
		return Hora(hh,mm,ss)
		
	def __bool__(self):
		return self.segundos() != 0
		
	def __call__(self):
		print(str(self))
		
