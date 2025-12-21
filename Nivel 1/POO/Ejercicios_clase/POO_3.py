# Plantear una clase Persona que contenga dos atributos: nombre y edad. Definir como
# responsabilidades la carga por teclado y su impresión.
# En el bloque principal del programa definir un objeto de la clase persona y llamar a sus métodos.
# Declarar una segunda clase llamada Empleado que herede de la clase Persona y agregue un atributo
# sueldo y muestre si debe pagar impuestos (sueldo superior a 3000)

# class Persona:

#     def __init__(self, nombre, edad):
#         self.__nombre = nombre
#         self.__edad = edad

#     # def toma_de_datos(self, datos):
#     #     nombre, edad = datos
#     #     self.__nombre = nombre
#     #     self.__edad = edad

#     @property
#     def devolver_atributos(self):
#         atributos = self.__nombre, self.__edad
#         return atributos

# class Empleado(Persona):

#     def __init__(self, nombre, edad, sueldo):
#         super().__init__(nombre, edad)
#         self.__sueldo = sueldo
    
#     def paga_impuestos(self, minimo):
#         if self.__sueldo > minimo:
#             return True

#     @property
#     def mostrar(self):
#         datos = super().devolver_atributos, self.__sueldo
#         return datos

# # MAIN
# def datos():
#     nombre = input('Ingresa el nombre: ')
#     edad = int(input('Ingresa la edad: '))
#     datos = nombre, edad
#     return datos

# sueldo = int(input('Ingresa el sueldo: '))
# minimo = 3000

# nombre, edad = datos()
# empleado = Empleado(nombre, edad, sueldo)
# # empleado.toma_de_datos(datos())
# if empleado.paga_impuestos(minimo):
#     print('Debe pagar impuestos')
# else:
#     print('Esta extento')

# print(empleado.mostrar)



# ------------------------------------------------- #

# Tu objetivo es crear una clase CuentaBancaria que gestione el saldo de un cliente.
# ------------------------------------------------- #
# class Sujeto:

#     def __init__(self, nombre, id):
#         self.__nombre = nombre
#         self.__id = id
#         self.__saldo = 0

#     def ingresar_dinero(self, monto):
#         self.__saldo += monto
    
#     def sacar_dinero(self, monto):
#         if self.__saldo > monto:
#             self.__saldo = self.__saldo - monto
#         else:
#             print('La operacion no es posible')

#     @property
#     def mostrar_saldo(self):
#         return self.__saldo

# class Banco(Sujeto):

#     def __init__(self, datos):
#         nombre, id = datos
#         self.__cliente = super().__init__(nombre, id)

# # MAIN

# def crear_cuenta():
#     nombre = input('Ingresa el nombre de la persona: ')
#     id = input('Ingresa el documento de la persona: ')
#     datos = nombre, id
#     return datos

# def monto():
#     monto = int(input('Ingresa el monto: '))
#     return monto

# nueva_cuenta = Banco(crear_cuenta())
# nueva_cuenta.ingresar_dinero(monto())
# nueva_cuenta.sacar_dinero(monto())
# print('Saldo actual:', nueva_cuenta.mostrar_saldo)



# ------------------------------------------------- #





# ------------------------------------------------- #


# calcular cuánto se le debe pagar a distintos tipos de empleados en una empresa. 
# Cada tipo de empleado calcula su sueldo de forma diferente.

# La Jerarquía de Clases

#     Clase Base Empleado (Abstracta):
#         Atributos: nombre, id_empleado.
#         Método calcular_pago(): Debe estar definido pero no implementado 
# (puedes usar pass o lanzar un error), ya que cada subclase lo hará de forma distinta.

#     Subclase EmpleadoAsalariado:
#         Atributo extra: sueldo_mensual.
#         Su pago es simplemente su sueldo mensual fijo.

#     Subclase EmpleadoPorHora:
#         Atributos extras: horas_trabajadas, tarifa_por_hora.
#         Su pago se calcula como horas_trabajadas×tarifa_por_hora.

#     Subclase EmpleadoComision:
#         Atributos extras: sueldo_base, ventas_realizadas, tasa_comision.
#         Su pago es sueldo_base+(ventas_realizadas×tasa_comision).

