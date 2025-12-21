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

# Clases x

# Clase 27

indexacuin y slicing en numpy
pdf numpy3

caso 3d
```py
arr3d = np.array([[[1,2][3,4]][[5,6][7,8]]])
print(arr3d)
print(arr3d[0, 1, 1]) #Se imprime del primer bloque, segunda fila, segunda columna que es:4
#Para ver el bloque completo:
print(arr3d[1, :, :]) # segundo bloque que seria [[5,6][7,8]]
```
el slicing es sectorizar un dato, puede ser tanto particular como tambien un grupo


__numpy4.pdf__:

4. Operaciones básicas con array
```py
import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40]) # Tanto a como b son vectores

print("Suma:", a + b) # [11 22 33 44]
print("Resta:", b - a) # [ 9 18 27 36]
print("Multiplicación:", a * b) # [ 10 40 90 160]
print("División:", b / a) # [10. 10. 10. 10.]
print("Potencia:", a ** 2) # [ 1 4 9 16]
```
Aclaración: Numpy se suele utilizar con grandes volumenes de datos, ya que hace operaciones en manera simultanea, mientras que de forma normal (con for) es ciclica

__broadcasting__:
Permite operar entre arrays de diferentes tamaños y formas
Ejemplo,sumar un escalar a un array:
```py
arr = np.array([1, 2, 3, 4])
print(arr + 5) # [6 7 8 9]
```
operacion entre dimensiones diferentes:
```py
mat = np.array([[1, 2, 3],
[4, 5, 6]])
vec = np.array([10, 20, 30])
print(mat + vec)

# [[11 22 33]
# [14 25 36]]
```
# Clase 28

numpy5: ARCHIVO MÁS IMPORTANTE O MÁS UTILIZADO

División de arrays

_Transposición y permutacion de ejes_:
es la transpuesta de una matriz
```py
import numpy as np

mat = np.array([[1, 2, 3],
[4, 5, 6]])
print("Matriz original:\n", mat)
print("Transpuesta:\n", mat.T)
```

__Selección y filtrado de datos__:
comentario: En el resoso es importante agarrarle más la mano a POO
Consiste en aplicar una condición lógica sobre un array. El resultado es otro array con valores True/False que usamos para filtrar.

```py
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

# Crear un filtro booleano
filtro = arr > 25
print("Filtro booleano:", filtro)

# Aplicar filtro al array
print("Elementos mayores a 25:", arr[filtro])
# Salida:
Filtro booleano: [False False True True True]
Elementos mayores a 25: [30 40 50]
```
Comentario: Este tipo de filtro, se usa mucho para tomar datos

_Mascaras_
Máscara simple
```py
arr = np.arange(1, 11) # [1 2 3 4 5 6 7 8 9 10]
mascara = arr % 2 == 0 # Números pares
print("Máscara:", mascara)
print("Números pares:", arr[mascara])

# Salida:
Máscara: [False True False True False True False True False True]
Números pares: [ 2 4 6 8 10]
```

Máscara combinada
Podemos combinar condiciones con operadores lógicos: *&* (AND), *| (no '/')* (OR) y *~* (NOT).
```py
# Seleccionar números mayores a 3 y menores a 8
arr = np.arange(1, 11)
mascara = (arr > 3) & (arr < 8)
print("Condición (3 < arr < 8):", arr[mascara])

#Salida:
Condición (3 < arr < 8): [4 5 6 7]
```

__Filtrado condicional con np.where__
np.where devuelve los índices donde se cumple una condición.
_Obtener índices_:
```py
arr = np.array([5, 10, 15, 20, 25])
indices = np.where(arr > 12)
print("Índices de elementos > 12:", indices)
print("Elementos:", arr[indices])

#Salida:
Índices de elementos > 12: (array([2, 3, 4]),)
Elementos: [15 20 25]
```
_If vectorizado_
```py
# Podemos usar np.where(condición, valor_si_verdadero, valor_si_falso).
arr = np.array([5, 10, 15, 20, 25])

# Si el elemento es mayor a 15 "Alto", si no "Bajo"
resultado = np.where(arr > 15, "Alto", "Bajo")
print("Clasificación:", resultado)

# Salida:
Clasificación: ['Bajo' 'Bajo' 'Bajo' 'Alto' 'Alto']
```
### Estadísticas y funciones de agregación
__Mínimo y máximo__
Con np.min() y np.max() obtenemos el valor más bajo y más alto de un array.
```py
import numpy as np

arr = np.array([5, 12, 7, 20, 15])
print("Mínimo:", np.min(arr)) # 5
print("Máximo:", np.max(arr)) # 20

# También existen los métodos👉 .min() y .max() que funcionan igual que es de python base:
print("Mínimo (método):", arr.min())
print("Máximo (método):", arr.max())
```
Ver media y mediana, desviacion y suma y productos

__Numpy6__ (Es importante, pero aun no se va a ver en profundidad, recomendable ver de todos modos)

__Numpy7__
_Generación de números aleatorios ( np.random )_
Existen múltiples formas de generar números aleatorios:
a. Un número aleatorio entre 0 y 1 ( random.rand )
```py
import numpy as np
print("Número aleatorio [0,1):", np.random.rand())
```

_Distribuciones_
Distribución uniforme ( np.random.uniform )
Genera valores entre un rango [a, b) con probabilidad uniforme.
```py
arr = np.random.uniform(0, 10, size=5)
print("Distribución uniforme [0,10):", arr)
```

Distribución normal o gaussiana ( np.random.normal )
Muy utilizada en estadística y machine learning.
```py
arr = np.random.normal(loc=0, scale=1, size=10)
print("Distribución normal (media=0, std=1):", arr)
```
