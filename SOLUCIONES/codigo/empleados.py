# Gestion de empleados:
import sqlite3 as dbapi

class Empleado():
	
	def __init__(self,dni="",nom="",dpo="",t=None):
		if t == None:
			self.dni = dni
			self.nom = nom
			self.dpo = dpo
		else:
			self.dni = t[0]
			self.nom = t[1]
			self.dpo = t[2]
		
	def toTuple(self, n=0):
		if n == 0:
			return (self.dni, self.nom, self.dpo)
		else:
			return (self.nom, self.dpo, self.dni)
		
	def __str__(self):
		return self.dni+' '+self.nom+' '+self.dpo
		
	def __repr__(self):
		return self.dni+' '+self.nom+' '+self.dpo
		
class EmpleadoBD():
	
	def __init__(self, fichero):
		self.con = dbapi.connect(fichero)
		self.cur = self.con.cursor()
		
	def create(self,emp):
		sql = """insert into 
		empleados(dni,nombre,departamento) 
		values(?,?,?)"""
		self.cur.execute(sql, emp.toTuple())
		self.con.commit()
		
	def delete(self,dni):
		sql = "delete from empleados where dni=?"
		self.cur.execute(sql, (dni,))
		self.con.commit()
		
	def update(self,emp):
		sql = """update empleados set nombre=?,
		departamento=? where dni=?"""
		self.cur.execute(sql, emp.toTuple(1))
		self.con.commit()		
		
	def read(self,dni):
		sql = "select * from empleados where dni=?"
		self.cur.execute(sql,(dni,))
		temp = self.cur.fetchone()
		if temp != None:
			return Empleado(t=temp)
		else:
			return None
		
	def selectAll(self):
		lista = []
		sql = "select * from empleados"
		self.cur.execute(sql)
		for tup in self.cur.fetchall():
			lista.append(Empleado(t=tup))
			
		return lista
		
	def desconectar(self):
		if self.cur != None: self.cur.close()
		if self.con != None: self.con.close()
	
if __name__=='__main__':
	bd = EmpleadoBD('bbdd.dat')
	# Crear emp:
	bd.create(Empleado('1','AAA','DPO1'))
	emp = bd.read('1')
	print('Emp: ', emp)
	emp.nombre='Pepe'
	bd.update(emp)
	# Recuperar todos:
	L = bd.selectAll()
	print("\nEmpleados:")
	for e in L:
		print(e)
	bd.desconectar()
