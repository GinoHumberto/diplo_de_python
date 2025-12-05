# Clase 20
## Base de SQL
Imaginemos una plantilla de excel. Cada cuadro se llama campo. Un campo puede tener un titulo (un contenido).
Por ej 
tenemos el campo "Nombre", todo lo que haya en la columna del campo nombre es lo que se donomina un "Registro".

El registro puede ser un numero, id, nombre, etc.

Las tablas pueden relacionarse con otras

SQL es un lenguaje o gestor de base de datos "Relacional" para base de datos __ESTRUCTURADA__, es decir deben estar en orden.
Cada registro esta determinado por un ID

__COMO TRABAJAR CON MYSQL__
```py
import sqlite3

conexion=sqlite3.connect("bd1.db")
try:
    conexion.execute("""create table articulos (
                            codigo integer primary key autoincrement,
                            descripcion text,
                            precio real
                        )""")
    print("se creo la tabla articulos")
except sqlite3.OperationalError:
    print("La tabla articulos ya existe")
conexion.close()
```



Cuando no conectamos con una base de datos, se crea una localmente


Para conectarse a una base no local se necesita SQL
MYSQL se conecta a una base local no una base que sea sacada de un servidor

Hay funciones importantes como: create_table

Para poder trabajar con bases de datos de tipo SQLite debemos primero importar el módulo 'sqlite3':
__import sqlite3__ 

Para crear o abrir una conexión con una base de datos existente debemos llamar a la función 'connect' del módulo 'sqlite3':
__conexion=sqlite3.connect("nombre_de_la_base.db")__

La primera vez que ejecutemos este programa como no existe la base de datos 'bd1.db' se crea, consiste en un único archivo que se localiza en la misma carpeta de nuestra aplicación


### Como modificar la tabla:
```py
import sqlite3
conexion=sqlite3.connect("bd1.db")
conexion.execute("insert into articulos(descripcion,precio) values (?,?)",
("naranjas", 23.50))
conexion.execute("insert into articulos(descripcion,precio) values (?,?)",
("peras", 34))
conexion.execute("insert into articulos(descripcion,precio) values (?,?)",
("bananas", 25))
conexion.commit()
conexion.close()
```

### Recuperar todas las filas de una tabla
Es a lo que se le llama consulta, nos muestra las filas
```py
import sqlite3

conexion=sqlite3.connect("bd1.db")
cursor=conexion.execute("select codigo,descripcion precio from articulos") # Cursor esta guardando toda la consulta
for fila in cursor:
    print(fila)
conexion.close()

# Nos va a devolver si hubieramos echo lo anterior

# (1, 'naranjas', 23.5 )
# (2, 'peras', 34.0 )
# (3, 'bananas', 25.0 )
```

### Recuperar 1 fila de una tabla
```py
import sqlite3

conexion=sqlite3.connect("bd1.db")
codigo=int(input("Ingrese el código de un artículo:"))
cursor=conexion.execute("select descripcion,precio from articulos where codigo=?", (codigo, ))

fila=cursor.fetchone() # Es un método en Python que se usa para recuperar la siguiente fila(cursor) de un conjunto de resultados de una consulta de base de datos
                       # Es decir retorna una tupla con la fila de la tabla que coincide con el codigo ingresado
if fila!=None:
    print(fila)
else:
    print("No existe un artículo con dicho código.")
conexion.close()
```

### Recuperar varias filas de una tabla
```py
import sqlite3

conexion=sqlite3.connect("bd1.db")
precio=float(input("Ingrese un precio:"))
cursor=conexion.execute("select descripcion from articulos where precio<?", (precio, ))

filas=cursor.fetchall() # fetchall nos retorna una lista con todas las filas de la tabla que cumplan la condición en este caso precio 
if len(filas)>0:
    for fila in filas:
        print(fila)
else:
    print("No existen artículos con un precio menor al ingresado.")
conexion.close()
```

# Tarea para jueves
Traer un ejemplo donde pueda modificar los datos y uno donde se tenga que eliminar
leer: https://docs.python.org/3/library/dbm.html#module-dbm.sqlite3

# Clase 21
## Introduccion a la ciencia de datos
Es la disciplina que combina programación, estadística y conocimiento del dominio para extraer valor accionable a partir de datos.

Es la integracion de utilizar herramientas para convertir datos en decisiones medibles.

#### IMPORTANTE OBJETIVO DE CIENCIA DE DATOS E IA
__Describir__: entender qué ocurrió (métricas, tendencias, segmentos).

__Diagnosticar__: explicar por qué ocurrió (correlaciones, factores causales plausibles).

__Predecir__: estimar qué puede ocurrir (modelos supervisados).

__Prescribir__: recomendar qué hacer (optimización, simulación, reglas de decisión).

__Monitorear__: seguir el desempeño y detectar desvíos (tableros, alertas).

__Mejorar__: cerrar el ciclo con experimentación (A/B testing, iteración del modelo).


# Clase 22

## Instalación de Xampp (importante instalar)

__IMPORTANTE__: Instalar en un entorno virtual

Descargarse una version mas vieja (que venga con mySQL) Recomendacion: 5.6.XX Ej: 5.6.40 <-

Clase basada en Xampp

# Clase 23

Ver si instalar jupyter

Librerias que se van a utilizar:

__numpy__: libreria para calculo numérico eficiente, trabaja con matrices.
Ej:
```py
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Suma:", a + b)
print("Producto punto:", np.dot(a, b))
```

__pandas__: Para series y dataframe(permite manipular o incorporar datos de diferentes origenes y transformarlos una ves analizados.)
Ej:
```py
import pandas as pd

# Crear un DataFrame
data = {
"Nombre": ["Ana", "Luis", "Carla"],
"Edad": [23, 30, 27],
"Ciudad": ["Córdoba", "Rosario", "Mendoza"]
}
df = pd.DataFrame(data)
print(df)
print(df.describe()) # Estadísticas básicas
```

__Matplotlib__: Permite visualizar, crea graficos.
Ej:
```py
import matplotlib.pyplot as plt # Aca utilizamos pyplot, por eso el .pyplot, es lo mismo que usar "from matplotlib import pyplot"

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y, marker="o")
plt.title("Gráfico simple")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.show()
```

__scikit-learn__: Incluye algoritmos listos para regresión, clasificación, clustering y herramientas para evaluar modelos.
Ej:
```py
from sklearn.linear_model import LinearRegression

import numpy as np
# Datos ficticios
x = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([2, 4, 6, 8, 10])
modelo = LinearRegression()
modelo.fit(x, y)
print("Pendiente:", modelo.coef_)
print("Intersección:", modelo.intercept_)
print("Predicción para 6:", modelo.predict([[6]])[0])
```