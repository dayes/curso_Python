# clase hora:
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
		
class Fecha:
	
	def __init__(self, d=1,m=1,y=1970):
		self.d = d
		self.M = m
		self.y = y
		
	def __str__(self):
		return str("%02d/%02d/%d" % (self.d,self.M,self.y))
		
	def __repr__(self):
		return str("%02d/%02d/%d" % (self.d,self.M,self.y))

# Con herencia Multiple		
class FechaHora(Fecha,Hora):
	
	def __init__(self, d=1,m=1,y=1970, h=0, M=0,s=0):
		Fecha.__init__(self, d,m,y)
		Hora.__init__(self,h,M,s)
		
	def __str__(self):
		return Fecha.__str__(self) + ' ' + Hora.__str__(self)
		
	def __repr__(self):
		return Fecha.__repr__(self) + ' ' + Hora.__repr__(self)

# Con Composicion:	
class FechaHora2:
	
	'''
	def __init__(self, fecha = Fecha(), hora = Hora()):
		self.fecha = fecha
		self.hora = hora
	'''
	def __init__(self, fecha = None, hora = None, \
	d=1,m=1,y=1970, h=0, M=0,s=0):
		if fecha == None:
			self.fecha = Fecha(d,m,y)
		else:
			self.fecha = fecha
			
		if hora == None:
			self.hora = Hora(h,M,s)
		else:
			self.hora = hora
	
	def __str__(self):
		return str(self.fecha) + ' ' + str(self.hora)
		
	def __repr__(self):
		return repr(self.fecha) + ' ' + repr(self.hora)

if __name__ == '__main__':
	
	f3 = FechaHora2()
	print(f3)
	
	f3 = FechaHora2(hora = Hora(5,6,7))
	print(f3)
	
	f3 = FechaHora2(h=5,M=6,s=7)
	print(f3)
	
	f2 = FechaHora(s = 40)
	print(f2)
	
	f1 = Fecha()
	print(f1)
	
	h1 = Hora(3)
	h2 = Hora(1,1,1)
	h3 = Hora(8,30)
	h4 = Hora(4,55,6)
	
	h1()
	
	if h1:
		print('h1 es true')
	else:
		print('h1 false')
	
	L = [h1,h2,h3,h4]
	L.sort(reverse=True)
	
	r = h1 + h2
	print(r)
	print(L)
	

