# Clase declarativas. Empleado
class Empleado(object):
    # Variable estatica (Para todas las instancias)
    numEmpleados = 0
    # Constructor
    def __init__(self,nombre="",empresa="",sueldo=0.0):
        self.nombre = nombre
        self.sueldo = sueldo
        self.empresa = empresa
        self.proyectos = []
        # Cada vez que se crea un empleado suma a la variable estatica
        Empleado.numEmpleados += 1

    # Funcion para acceso a proyectos que no esta en construcctor
    def asignarProyecto(self, proyecto):
        self.proyectos.append(proyecto)

    #Metodo estatico
    @staticmethod
    def numeroEmpleados():
        return Empleado.numEmpleados

    # El toString de java
    def __str__(self):
        return self.nombre + " " + self.empresa + " " + \
            str(self.sueldo) + " " + str(self.proyectos)
    
    # El toString para listas
    def __repr__(self):
        return self.nombre + " " + self.empresa + " " + \
            str(self.sueldo) + " " + str(self.proyectos)

class JefeDeProyecto(Empleado):
    """
    Clase que hereda de la anterior
    """
    def __init__(self,nombre="",empresa="",sueldo=0.0,empleados=[]):
        Empleado.__init__(self,nombre,empresa,sueldo)
        self.empleados = empleados
    
    # Sobreescrbir el método del padre
    def __str__(self):
        return super().__str__() + " Empleados: " + str(self.empleados)

# Inicio del programa
if __name__ == "__main__":
    #Creamos empleados
    emp = Empleado("Andres","TNT",2000.0)
    emp2 = Empleado("David","GC",5000.0)
    emp3 = Empleado("Mamerto","TNT",1000.0)
    # Asignamos proyectos a 1
    emp.asignarProyecto("Aplicacion WEB")
    # Lista de empleados
    empleados = [emp,emp2,emp3]
    # Impresión con str
    for i in empleados:
        print(i)
    # Impresión con repr
    print(empleados)
    print(emp.numeroEmpleados())
    jefe = JefeDeProyecto("Sara","TNT",5000,[emp,emp2,emp3])
    print(jefe)