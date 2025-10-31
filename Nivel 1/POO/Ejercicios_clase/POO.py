# Implementaremos una clase llamada Persona que tendrá como atributo (variable) su nombre y dos
# métodos (funciones), uno de dichos métodos inicializará el atributo nombre y el siguiente método
# mostrará en la pantalla el contenido del mismo.

'''
class Persona:

    def __init__(self):
        self.nombre = input('Ingresa el nombre de la persona: ')

    def mostrar(self):
        print('Nombre:', self.nombre)

persona1 = Persona()
persona1.mostrar()
'''

# Implementar una clase llamada Alumno que tenga como atributos su nombre y su nota. Definir los
# métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje si está regular (nota mayor o igual a 4)
# Definir dos objetos de la clase Alumno

'''
class Alumno:

    def __init__(self):
        self.nombre = input('Ingresa el nombre del alumno: ')
        self.nota = int(input('Ingresa la nota del alumno: '))

    def mostrar(self):
        print(self.nombre)
        print(self.nota)
        print(self.regularidad())

    def regularidad(self):
        if self.nota >= 4:
            return 'Regular'
        else: 
            return 'Irregular'

alumno = Alumno()
alumno.mostrar()
'''

# Confeccionar una clase que permita carga el nombre y la edad de una persona. Mostrar los
# datos cargados. Imprimir un mensaje si es mayor de edad (edad>=18)

'''
class Persona:

    def __init__(self):
        self.nombre = input('Ingresa el nombre: ')
        self.edad = int(input('Ingresa la edad: '))
    
    def mostrar(self):
        print(self.nombre)
        print(self.edad)
        print(self.mayor_de_edad())
    
    def mayor_de_edad(self): 
        if self.edad > 17:
            return 'Es mayor de edad'
        else:
            return 'Es menor de edad'

persona = Persona()
persona.mostrar()
'''

# Desarrollar un programa que cargue los lados de un triángulo e implemente los siguientes
# métodos: inicializar los atributos, imprimir el valor del lado mayor y otro método que
# muestre si es equilátero o no. El nombre de la clase llamarla Triangulo.

'''
class Triangulo:

    def __init__(self):
        self.lado_1 = int(input('Ingresa el largo del lado: '))
        self.lado_2 = int(input('Ingresa el largo del lado: '))
        self.lado_3 = int(input('Ingresa el largo del lado: '))

    def mayor(self):
        if self.lado_1 > self.lado_2 and self.lado_1 > self.lado_3:
            return 'El lado 1 es mayor'
        elif self.lado_2 > self.lado_1 and self.lado_2 > self.lado_3:
            return 'El lado 2 es mayor'
        elif self.lado_3 > self.lado_1:
            return 'El lado 3 es mayor'
        else:
            return 'No hay mayor'
    
    def equilatero(self):
        if self.lado_1 == self.lado_2 and self.lado_1 == self.lado_3:
            return 'Es equilatero'
        else:
            return 'No es equilatero'
    
    def mostrar(self):
        print(self.mayor())
        print(self.equilatero())

triangulo = Triangulo()
triangulo.mostrar()
'''

# Confeccionar una clase que represente un empleado. Definir como atributos su nombre y su sueldo.
# En el método __init__ cargar los atributos por teclado y luego en otro método imprimir sus datos y
# por último uno que imprima un mensaje si debe pagar impuestos (si el sueldo supera a 3000)

'''
class Empleado:

    def __init__(self):
        self.nombre = input('Ingresa el nombre: ')
        self.sueldo = int(input('Ingresa el sueldo: '))
    
    def impuestos(self):
        if self.sueldo > 3000:
            return 'Debe pagar impuestos'
        else:
            return 'No debe pagar impuestos'
        
    def mostrar(self):
        print(self.nombre)
        print(self.sueldo)
        print(self.impuestos())

empleado = Empleado()
empleado.mostrar()
'''

# Plantear una clase Operaciones que solicite en el método __init__ la carga de dos enteros e
# inmediatamente muestre su suma, resta. Hacer cada operación en otro
# método de la clase Operación y llamarlos desde el mismo método __init_

'''
class Operaciones:

    def __init__(self):
        self.valor1 = int(input('Ingresa tu primer valor: '))
        self.valor2 = int(input('Ingresa tu primer valor: '))
        self.sumar()
        self.restar()
    
    def sumar(self):
        print(self.valor1 + self.valor2)
    
    def restar(self):
        print(self.valor1 - self.valor2)

operacion = Operaciones()
'''

# Plantear una clase que administre dos listas de 5 nombres de alumnos y sus notas. Mostrar un menú
# de opciones que permita:
# 1- Cargar alumnos.
# 2- Listar alumnos.
# 3- Mostrar alumnos con notas mayores o iguales a 7.
# 4- Finalizar programa.

'''
class Alumnos:

    def __init__(self):
        self.nombres=[]
        self.notas=[]
    
    def menu(self):
        opcion = 0
        while opcion != 4:
            self.menu = print(' 1- Cargar alumnos. \n 2- Listar alumnos. \n 3- Mostrar alumnos con notas mayores o iguales a 7. \n 4- Finalizar programa.')
            opcion = int(input('¿Qué deseas hacer? '))
            if opcion == 1:
                self.cargar()
            elif opcion == 2:
                self.listar()
            elif opcion == 3:
                self.buenas_notas()
    
    def cargar(self):
        for alumno in range(5):
            nombre = input('Ingrese el nombre del alumno: ')
            notas = int(input('Ingresa la nota del alumno: '))
            self.nombres.append(nombre)
            self.notas.append(notas)
    
    def listar(self):
        for i in range(5):
            print(self.nombres[i], self.notas[i])
    
    def buenas_notas(self):
        buena_nota = 0
        for i in range(5):
            if self.notas[i] >= 7:
                buena_nota += 1
        print(buena_nota)

alumnos = Alumnos()
alumnos.menu()
'''

# Confeccionar una clase que administre una agenda personal. Se debe almacenar el nombre
# de la persona, teléfono y mail
# Debe mostrar un menú con las siguientes opciones:
# 1- Carga de un contacto en la agenda.
# 2- Listado completo de la agenda.
# 3- Consulta ingresando el nombre de la persona.
# 4- Modificación de su teléfono y mail.
# 5- Finalizar programa.

# class Agenda:

#     def __init__(self):
#         self.nombre = []
#         self.telefono = []
#         self.mail = []
    
#     def menu(self):
#         choice = 0
#         while choice != 5:
#             print(' 1- Carga de un contacto en la agenda. \n 2- Listado completo de la agenda. \n 3- Consulta ingresando el nombre de la persona. \n 4- Modificación de su teléfono y mail. \n 5- Finalizar programa.')
#             print('----------------------------------------')
#             choice = int(input('¿Qué opción quieres elegir?: '))
#             if choice == 1:
#                 self.cargar()
#             elif choice == 2:
#                 self.listado()
#             elif choice == 3:
#                 self.consulta()
#             elif choice == 4:
#                 self.modificar()
    
#     def cargar(self):
#         name = input('Ingresa el nombre de la persona: ')
#         nombre = name.capitalize()
#         telefono = input('Ingresa el numero de telefono: ')
#         mail = input('Ingresa el mail: ')
#         self.nombre.append(nombre)
#         self.telefono.append(telefono)
#         self.mail.append(mail)
    
#     def listado(self):
#         for i in range (len(self.nombre)):
#             print(f'Persona: {self.nombre[i]} \n Telefono: {self.telefono[i]} \n mail: {self.mail[i]}')
    
#     def consulta(self):
#         print('Ingresa el nombre con mayuscula')
#         busqueda = input('Ingresa el nombre de la persona que buscas: ')
#         print('~~~~~~~~~~~~~~~~')
#         search = busqueda.capitalize()
#         encontrado = 0
#         for i in range(len(self.nombre)):
#             if search == self.nombre[i]:
#                 print('Lo encontramos, es: ')
#                 print(f'Persona: {self.nombre[i]} \n Telefono: {self.telefono[i]} \n mail: {self.mail[i]}')
#                 encontrado = 1
#         if encontrado == 0:
#             print('No se encontro dicha persona, intenta de nuevo')
    
#     def modificar(self):
#         print('¿A quien deseas modificar?')
#         who = input('Ingresa el nombre de la persona ')
#         for i in range(len(self.nombre)):
#             if who == self.nombre[i]:
#                 print('Estos son sus datos actuales: ')
#                 print(f'Persona: {self.nombre[i]} \n Telefono: {self.telefono[i]} \n mail: {self.mail[i]}')
#                 print('~~~~~~~~~~~~~~')
#                 nuevo_telefono = int(input('Ingresa el nuevo telefono: '))
#                 nuevo_mail = input('Ingresa el nuevo mail')
#                 self.telefono[i] = nuevo_telefono
#                 self.mail[i] = nuevo_mail

# agenda = Agenda()
# agenda.menu()

# Corrección
#--------------------------------------------------------------------------------------------------#

class Persona:
    def __init__(self,nombre,telefono,mail):
        self._nombre = nombre   # el _ antes del nombre del atributo es una buena practica [ver 1]
        self._telefono = telefono
        self._mail = mail

    # [1]: Los guiones "_" denotan que un atributo es privado (no se puede accdeder desde afuera de la clase).
    #   Acceder a estos atributos privados es como entrar a la casa de alguien a preguntarle su nombre (sin permiso)
    #   Entonces, lo correcto es hacer los metodos "getter" que como el nombre dice, te permiten acceder a atributos
    #   privados expuestos a propósito, como el de abajo 

    @property
    def nombre(self):
        return self._nombre

    def modificar(self, new_mail, new_tel):
        self._telefono = new_tel
        self._mail = new_mail

    def __str__(self):
        return f'Nombre: {self._nombre}; Telefono: {self._telefono}; Mail: {self._mail}' #Conversion de persona a str

class Agenda:
    def __init__(self):
        self._contactos = {}

    def add(self,persona:Persona): # Acá le decimos que persona (la variable) es de tipo Persona (la clase)
        self._contactos[persona.nombre] = persona

    def consulta(self, nombre):
        return self._contactos.get(nombre) # es como self._contactos[nombre] pero no falla si no existe la key del diccionario _contactos

    def modificar(self, nombre): # el nombre debe existir en el diccionario
        persona = self._contactos.get(nombre)
        if persona:
            new_tel = input('Nuevo telefono: ')
            new_mail = input('Nuevo mail: ')
            persona.modificar(new_tel,new_mail)

    def __str__(self):
        agenda = 'Agenda\n'
        for nombre in self._contactos:  # Agenda puede acceder a contactos porque está en su propia casa
            agenda += str(self._contactos[nombre]) + '\n'
        return agenda

def crear_persona():
    nombre = input('Nombre: ')
    telefono = input('Telefono: ')
    mail = input('Mail: ')
    return Persona(
        nombre=nombre,
        telefono=telefono,
        mail=mail
        )

def menu(agenda:Agenda):
    options = '''
     1- Carga de un contacto en la agenda. \n 
     2- Listado completo de la agenda. \n 
     3- Consulta ingresando el nombre de la persona. \n 
     4- Modificación de su teléfono y mail. \n 
     5- Finalizar programa. \n
     ----------------------------------------
    '''
    choice = 0
    while choice != 5:
        print(options)
        choice = int(input('¿Qué opción quieres elegir?: '))
        if choice == 1:
            persona = crear_persona()
            agenda.add(persona)
        elif choice == 2:
            print(agenda)
        elif choice == 3:
            nombre = input('Nombre del contacto: ')
            contacto = agenda.consulta(nombre)
            print(contacto)
        elif choice == 4:
            nombre = input('Nombre del contacto: ')
            agenda.modificar(nombre)

# Esta es la parte más importante del código
agenda = Agenda()   # Creamos una agenda vacía
menu(agenda)        # Llamamos al menu con la agenda de arriba