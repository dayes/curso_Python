""" Ejemplo de polimorfismo parametrico"""

class tablaBaremos:
	
	def __init__(self, ipc, extras, objetivos, incentivos):
		self.ipc = ipc
		self.extras = extras
		self.objetivos = objetivos
		self.incentivos = incentivos
	

class personal:
	
	def __init__(self, nombre, apellidos, codigo, sueldo):
		self.nombre = nombre
		self.apellidos = apellidos
		self.codigo = codigo
		self.sueldo = sueldo
		
	def subirSueldo(self, tabla):
		raise Exception('Funcion no implementada')
		
	def __str__(self):
		return self.nombre + ", " + self.apellidos + ", " + str(self.codigo) + ", " + str(self.sueldo)

		
		
class director(personal):
	
	def __init__(self, nombre, apellidos, codigo, sueldo, beneficios, objetivos):
		super().__init__(nombre, apellidos, codigo, sueldo)
		self.beneficios = beneficios
		self.objetivos = objetivos
		
	def subirSueldo(self, tabla):
		self.sueldo = self.sueldo * (1 + (tabla.ipc/100))
		self.objetivos += tabla.objetivos
		self.beneficios += tabla.incentivos
		print("\ndirector.subirSueldo")
		return self.sueldo+self.objetivos+self.beneficios
		
	def __str__(self):
		return super().__str__() + ", " + str(self.beneficios) + ", " + str(self.objetivos)
		
	
		
class administrativo(personal):
	
	def __init__(self, nombre, apellidos, codigo, sueldo, extra1, extra2):
		super().__init__(nombre, apellidos, codigo, sueldo)
		self.extra1 = extra1
		self.extra2 = extra2
		
	def subirSueldo(self, tabla):
		self.sueldo = self.sueldo * (1 + (tabla.ipc/100))
		self.extra1 = self.extra1 * (1 + (tabla.extras/100))
		self.extra2 = self.extra2 * (2 + (tabla.extras/100))
		print("\nadministrativo.subirSueldo")
		return self.sueldo+self.extra1+self.extra2

	def __str__(self):
		return personal.__str__(self) + ", " + str(self.extra1) + ", " + str(self.extra2)
		
	
		
class jefeDeProyecto(personal):
	def __init__(self, nombre, apellidos, codigo, sueldo, incentivos):
		super().__init__(nombre, apellidos, codigo, sueldo)
		self.incentivos = incentivos
		
	def subirSueldo(self, tabla):
		self.sueldo = self.sueldo * (1 + (tabla.ipc/100))
		self.incentivos += tabla.incentivos		
		print("\njefeDeProyecto.subirSueldo")
		return self.sueldo+self.incentivos

	def __str__(self):
		return personal.__str__(self) + ", " + str(self.incentivos)
		
		
class empresa:
	
	def __init__(self):
		self.emp = []
		
	def add(self, empleado):
		self.emp.append(empleado)
		
	def __str__(self):
		resul = ""
		for e in self.emp:
			resul += e + "\n"			
		return resul
		
	def listar(self):
		for e in self.emp:
			print(e)
			
	def subirSueldo(self, tb):
		for e in self.emp:
			e.subirSueldo(tb)
		
if __name__=='__main__':
	tb = tablaBaremos(2.5, 3.5, 100, 250)
	emp = empresa()
	emp.add(director("aaa", "aaa", 1, 3000.0, 250, 500))
	emp.add(administrativo("bbb", "bbb", 2, 1000.0, 500, 500))
	emp.add(jefeDeProyecto("ccc", "ccc", 3, 2000.0, 1000))
	
	print("\n\nAntes de subir sueldo:")
	emp.listar()
	emp.subirSueldo(tb)
	print("\n\nDespues de subir sueldo:")
	emp.listar()
	
	#prueba de la excepcion:
	p = personal("aaa", "aaa", 1, 3000.0)
	p.subirSueldo(tb)
