# Traer un ejemplo donde pueda modificar los datos y uno donde se tenga que eliminar

# ¿Como modificar datos?

import sqlite3

# Creamos la base de datos

conexion = sqlite3.connect("Introduccion.db")
# Establecemos conexion y pasamos los campos
# conexion.execute(
#     """CREATE TABLE articulos (
#     codigo INTEGER PRIMARY KEY AUTOINCREMENT,
#     descripcion TEXT,
#     valor INTEGER)"""
# )
# Insertamos datos iniciales 
# conexion.execute("INSERT INTO articulos(descripcion,valor) values (?,?)", ("Hola", 11))
conexion.execute("INSERT INTO articulos(descripcion,valor) values (?,?)", ("Mundo", 25))

conexion.commit()

# Guardamos los datos en cursor para poder imprimir
cursor=conexion.execute("SELECT codigo,descripcion,valor FROM articulos")
print("Primer base\n")
for fila in cursor:
    print(fila)

# Modificamos la base
cursor.execute(
    """UPDATE articulos
    SET descripcion = ?
    WHERE codigo = ?
    """, ("Hola",1,)
)

conexion.commit()

cursor = conexion.execute("SELECT codigo, descripcion, valor FROM articulos")
print("\nBase Modificada\n")
for fila in cursor:
    print(fila)

# Para borrar
cursor.execute(
    """DELETE FROM articulos
    WHERE codigo = ?
    """, (2,)
)

conexion.commit()

cursor = conexion.execute("SELECT codigo, descripcion, valor FROM articulos")
print("\nBase sin la fila 2\n")
for fila in cursor:
    print(fila)

conexion.close()