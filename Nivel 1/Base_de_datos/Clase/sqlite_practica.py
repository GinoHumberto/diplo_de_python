# Vas a crear un programa que guarde nombres y teléfonos. 
# Lo haremos de forma que cada vez que cierres el programa y lo abras, los contactos sigan ahí.


import sqlite3

# def agregar_contacto():
#     nombre = input('Ingresa el nombre: ')
#     numero = int(input('Ingresa su número: '))
#     try:
#         cursor.execute('INSERT INTO agenda VALUES (?, ?)', (nombre, numero))
#         conexion.commit()
#         return True
#     except sqlite3.IntegrityError:
#         print(f'El nombre {nombre} ya esta en la agenda')

# def modificar_contacto(nombre, nuevo_numero):
#     cursor.execute(
#         '''UPDATE Agenda
#         SET numero = ?
#         WHERE nombre = ?''', (nuevo_numero, nombre)
#     )
#     conexion.commit()
#     return 'El contacto fue modificado con exito'

# def borrar_contacto(nombre):
#     cursor.execute(
#         '''DELETE FROM Agenda
#         WHERE nombre = ?''', (nombre, )
#     )
#     conexion.commit()
#     return 'El contacto fue borrado con exito'

# def mostrar():
#     mostrar = cursor.execute('SELECT nombre, numero FROM Agenda')
#     for fila in mostrar:
#         print(fila)

# def buscar_persona(nombre):
#     cursor.execute(
#         '''SELECT nombre, numero FROM Agenda
#         WHERE nombre = ?''', (nombre, )
#     )
#     print(cursor.fetchone())

# def menu():
#     return (
#         'Bienvenido al menu \n'
#         '1. Agregar contacto \n'
#         '2. Modificar contacto \n'
#         '3. Borrar contacto \n'
#         '4. Mostrar contactos \n'
#         '5. Buscar contacto por nombre \n'
#         '6. Salir'
#     )

# conexion = sqlite3.connect('Agenda.db')

# cursor = conexion.cursor()

# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS agenda (
#         nombre TEXT UNIQUE, numero REAL    
#     )
# ''')

# choice = 0
# while choice != 6:
#     print('\n', menu(), '\n')
#     choice = int(input('Seleciona una opción: '))
#     if choice == 1:
#         if agregar_contacto():
#             print('El contacto fue agregado con exito')
#     elif choice == 2:
#         nombre = input('Ingresa el nombre de la persona: ')
#         nuevo_numero = int(input('Ingresa el nuevo numero: '))
#         print(modificar_contacto(nombre,nuevo_numero))
#     elif choice == 3:
#         nombre = input('Ingresa a quien te gustaria borrar: ')
#         print(borrar_contacto(nombre))
#     elif choice == 4:
#         mostrar()
#     elif choice == 5:
#         nombre = input('Ingresa el nombre de la persona: ')
#         buscar_persona(nombre)
#     elif choice == 6:
#         conexion.close()



# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><> #

# Ejercicio: Inventario de Tienda "Mini-Stock"
# Vas a crear un sistema para una tienda pequeña.

class Tienda:

    def __init__(self):
        self.__conexion = sqlite3.connect('Tienda.db')
        self.__cursor = self.__conexion.cursor()
        self.__crear_tabla_producto = self.__cursor.execute(
            '''CREATE TABLE IF NOT EXISTS Productos (
                producto TEXT UNIQUE, precio REAL, cantidad INTEGER)'''
        )
        self.__crear_tabla_ventas = self.__cursor.execute(
            '''CREATE TABLE IF NOT EXISTS ventas(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                producto_vendido TEXT, cantidad INTEGER, 
                fecha TEXT DEFAULT CURRENT_TIMESTAMP)'''
        )

    def agregar_producto(self, producto, precio, cantidad):
        try:
            self.__cursor.execute(
                'INSERT INTO Productos VALUES (?, ?, ?)', (producto,precio,cantidad)
            )
            self.__conexion.commit()
        except sqlite3.IntegrityError:
            print('El producto ya existe')

    def modificar_precio(self, producto, nuevo_precio):
        self.__cursor.execute(
            '''UPDATE Productos
            SET precio = ?
            WHERE producto = ?''', (nuevo_precio, producto)
        )
        self.__conexion.commit()

    def vender(self, producto, cantidad_vendida):
        self.__cursor.execute(
            '''SELECT cantidad FROM Productos WHERE producto = ?''', (producto, )
        )
        resultado = self.__cursor.fetchone()
        if resultado:
            stock_actual = resultado[0]
            if stock_actual >= cantidad_vendida:
                nuevo_stock = stock_actual-cantidad_vendida
                self.__cursor.execute(
                    '''UPDATE Productos
                    SET cantidad = ?
                    WHERE producto = ? ''', (nuevo_stock, producto)
                )
                self.__conexion.commit()
            else:
                return 'No hay cantidades suficientes para esa venta'
        else:
            return 'El producto no existe'
        self.__cursor.execute(
            '''INSERT INTO ventas (producto_vendido, cantidad) 
                VALUES (?, ?)''', (producto, cantidad_vendida)
            )
        self.__conexion.commit()
    
    def agregar_stock(self, producto, cantidad_agregada):
        self.__cursor.execute(
            '''UPDATE Productos
            SET cantidad = cantidad + ?
            WHERE producto = ?''', (cantidad_agregada, producto)
        )
        self.__conexion.commit()

    def eliminar_producto(self, producto):
        self.__cursor.execute(
            '''DELETE FROM Productos 
            WHERE producto = ?''', (producto, )
        )
        self.__conexion.commit()

    def mostrar(self):
        mostrar = self.__cursor.execute('SELECT producto, precio, cantidad FROM Productos')
        for fila in mostrar:
            print(fila)

    def reporte(self):
        query = (
            '''SELECT v.fecha, v.producto_vendido, v.cantidad, P.precio, 
            (v.cantidad * P.precio) FROM ventas v
            INNER JOIN Productos P ON v.producto_vendido = P.producto'''
            )
        self.__cursor.execute(query)
        reporte = self.__cursor.fetchall()
        for fila in reporte:
            print(fila)

    def cerrar_conexion(self):
        self.__conexion.close()



# MAIN

tienda = Tienda()

def menu():
    print( 
        '\nBienvenido al menu \n'
        '1. Agregar producto \n'
        '2. Modificar precio \n'
        '3. Vender producto \n'
        '4. Agregar stock \n'
        '5. Eliminar producto \n'
        '6. Mostrar \n'
        '7. Reporte venta \n'
        '8. Cerrar conexion\n'
    )

choice = 0
while choice != 7:
    menu()
    choice = int(input('Que te gustaria hacer: '))
    if choice == 1:
        producto = input('Nombre del producto: ')
        precio = float(input('Ingresa el valor: '))
        cantidad = int(input('Ingresa la cantidad: '))
        tienda.agregar_producto(producto, precio, cantidad)
    elif choice == 2:
        producto = input('Ingresa el nombre del producto: ')
        nuevo_precio = int(input('Ingresa el nuevo precio: '))
        tienda.modificar_precio(producto, nuevo_precio)
    elif choice == 3:
        producto = input('Ingresa el nombre del producto: ')
        cantidad_vendida = int(input('Ingresa cuanto vendiste: '))
        tienda.vender(producto, cantidad_vendida)
    elif choice == 4:
        producto = input('Ingresa el nombre del producto: ')
        cantidad_agregada = int(input('Ingresa cuanto vas a agregar: '))
        tienda.agregar_stock(producto,cantidad_agregada)
    elif choice == 5:
        producto = input('Ingresa el nombre del producto: ')
        tienda.eliminar_producto(producto)
    elif choice == 6:
        tienda.mostrar()
    elif choice == 7:
        tienda.reporte()
    elif choice == 8:
        tienda.cerrar_conexion()
