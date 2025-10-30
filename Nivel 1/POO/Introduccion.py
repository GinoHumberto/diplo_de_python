'''
class Persona:

    def inicializar(self,nom):
        self.nombre=nom
    
    def imprimir(self):
        print("Nombre",self.nombre)


# bloque principal
persona1=Persona()
persona1.inicializar("Pedro")
persona1.imprimir()
persona2=Persona()
persona2.inicializar("Carla")
persona2.imprimir()
'''

'''
class Alumno:
    
    def inicializar(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota

    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Nota:",self.nota)

    def mostrar_estado(self):
        if self.nota>=4:
            print("Regular")
        else:
            print("Libre")


# bloque principal
alumno1=Alumno()
alumno1.inicializar("diego",2)
alumno1.imprimir()
alumno1.mostrar_estado()
alumno2=Alumno()
alumno2.inicializar("ana",10)
alumno2.imprimir()
alumno2.mostrar_estado()
'''
########################
#       __init__       #
########################
'''
class Empleado:

    def __init__(self):
        self.nombre=input("Ingrese el nombre del empleado: ")
        self.sueldo=float(input("Ingrese el sueldo:"))

    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Sueldo:",self.sueldo)

    def paga_impuestos(self):
        if self.sueldo>3000:
            print("Debe pagar impuestos")
        else:
            print("No paga impuestos")

# bloque principal
empleado1=Empleado()
empleado1.imprimir()
empleado1.paga_impuestos()
'''

# Metodo llamando metodos
'''
class Operacion:
    def __init__ (self):
        self.valor1 = int(input('Numero: '))
        self.valor2 = int(input('Numero: '))
        self.sumar()
        self.resta()
    
    def sumar(self):
        suma = self.valor1 + self.valor2
        print(suma)
    
    def resta(self):
        resta = self.valor1 - self.valor2
        print(resta)
    

operacion1 = Operacion()
'''
'''
class Cliente:

    def __init__(self,nombre):
        self.nombre=nombre
        self.monto=0

    def depositar(self,monto):
        self.monto=self.monto+monto

    def extraer(self,monto):
        self.monto=self.monto-monto

    def retornar_monto(self):
        return self.monto

    def imprimir(self):
        print(self.nombre,"tiene depositado la suma de",self.monto)

class Banco:

    def __init__(self):
        self.cliente1=Cliente("Juan")
        self.cliente2=Cliente("Ana")
        self.cliente3=Cliente("Diego")
    
    def operar(self):
        self.cliente1.depositar(100)
        self.cliente2.depositar(150)
        self.cliente3.depositar(200)
        self.cliente3.extraer(150)

    def depositos_totales(self):
        total=self.cliente1.retornar_monto()+self.cliente2.retornar_monto()+self.cliente3.retornar_monto()
        print("El total de dinero del banco es:",total)
        self.cliente1.imprimir()
        self.cliente2.imprimir()
        self.cliente3.imprimir()

# bloque principal
banco1=Banco()
banco1.operar()
banco1.depositos_totales()
'''

# Herencia
'''
class Persona:
    
    def __init__(self):
        self.nombre=input("Ingrese el nombre:")
        self.edad=int(input("Ingrese la edad:"))
    
    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Edad:",self.edad)

class Empleado(Persona):
    
    def __init__(self):
        super().__init__()
        self.sueldo=float(input("Ingrese el sueldo:"))
    
    def imprimir(self):
        super().imprimir()
        print("Sueldo:",self.sueldo)
    
    def paga_impuestos(self):
        if self.sueldo>3000:
            print("El empleado debe pagar impuestos")
        else:
            print("No paga impuestos")

# bloque principal
persona1=Persona()
persona1.imprimir()
print("____________________________")
empleado1=Empleado()
empleado1.imprimir()
empleado1.paga_impuestos()
'''
#variable:
class Persona:
    
    variable=20
    
    def __init__(self,nombre):
        self.nombre=nombre

# bloque principal
persona1=Persona("Juan")
persona2=Persona("Ana")
persona3=Persona("Luis")

print(persona1.nombre) # Juan
print(persona2.nombre) # Ana
print(persona3.nombre) # Luis
print(persona1.variable) # 20
Persona.variable=5
print(persona2.variable) # 5