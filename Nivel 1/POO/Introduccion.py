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
# class Persona:
#     
#     variable=20
#     
#     def __init__(self,nombre):
#         self.nombre=nombre
# 
# # bloque principal
# persona1=Persona("Juan")
# persona2=Persona("Ana")
# persona3=Persona("Luis")
# 
# print(persona1.nombre) # Juan
# print(persona2.nombre) # Ana
# print(persona3.nombre) # Luis
# print(persona1.variable) # 20
# Persona.variable=5
# print(persona2.variable) # 5

# class Cliente:
#     suspendidos=[]
# 
#     def __init__(self,codigo,nombre): #carga cliente de bloque.suspender
#         self.codigo=codigo
#         self.nombre=nombre
# 
#     def imprimir(self):
#         print("Codigo:",self.codigo)
#         print("Nombre:",self.nombre)
#         self.esta_suspendido()
# 
#     def esta_suspendido(self):
#         if self.codigo in Cliente.suspendidos:
#             print("Esta suspendido")
#         else:
#             print("No esta suspendido")
#         print("_____________________________")
# 
#     def suspender(self):
#         Cliente.suspendidos.append(self.codigo)
# 
# # bloque principal
# cliente1=Cliente(1,"Juan")
# cliente2=Cliente(2,"Ana")
# cliente3=Cliente(3,"Diego")
# cliente4=Cliente(4,"Pedro")
# 
# cliente3.suspender() # Suspendo aca
# cliente4.suspender()
# 
# cliente1.imprimir()
# cliente2.imprimir()
# cliente3.imprimir()
# cliente4.imprimir()
# 
# print(Cliente.suspendidos)

######## HERENCIA 2 ############

#class Operacion:
#    def __init__(self):
#        self.valor1=0
#        self.valor2=0
#        self.resultado=0
#    
#    def cargar1(self):
#        self.valor1=int(input("Ingrese primer valor:"))
#    
#    def cargar2(self):
#        self.valor2=int(input("Ingrese segundo valor:"))
#    
#    def mostrar_resultado(self):
#        print(self.resultado)
#    
#    def operar(self):
#        pass
#
#class Suma(Operacion):
#    
#    def operar(self):
#        self.resultado=self.valor1+self.valor2
#
#class Resta(Operacion):
#    
#    def operar(self):
#        self.resultado=self.valor1-self.valor2
#
## bloque princpipal
#suma1=Suma()
#suma1.cargar1()
#suma1.cargar2()
#suma1.operar()
#
#print("La suma de los dos valores es")
#suma1.mostrar_resultado()
#
#resta1=Resta()
#resta1.cargar1()
#resta1.cargar2()
#resta1.operar()
#
#print("La resta de los valores es:")
#resta1.mostrar_resultado()


######### METODO STR ###############
#class Persona:
#    
#    def __init__(self,nom,ape):
#        self.nombre=nom
#        self.apellido=ape
#    
#    def __str__(self):
#        cadena=self.nombre+","+self.apellido
#        return cadena
#        
#persona1=Persona("Jose","Rodriguez")
#print(persona1)

############ F string ################
# lista=[30.195, 400.2, 20.5555, 18.34, 67.0]
# for elemento in lista:
#     print(f"{elemento:10.2f}") # El 10 deja 10 caracteres de espacio, el .2f muestra una cantidad de decimales

############ Decorador ################
def decorador_saludo(funcion):
    def envoltura():
        print("¡Hola! Antes de ejecutar la función")
        funcion()
        print("¡Adiós! Después de ejecutar la función")
    return envoltura

@decorador_saludo
def saludar():
    print("Estoy saludando desde la función principal")
    
saludar()