# Clase 29

Tener en cuenta algunas clases vistas en el nivel 1 sobre numpy

Aclaraciones y habla sobre GIT

# Clase 30

Una rama en Git es para 2 grupos de trabajo, uno es para el main y el otro es para otro codigo.
Una rama es una forma de dividir las tares, haciendo que cada grupo trabaje en una rama, rama es una division de tareas.

**Pandas**
Trabaja con data frames, convierte los datos en algo muy facil de leer, organiza muy bien la informacion:
```py
import numpy as np
import pandas as pd

arr = np.array([10, 20, 30, 40, 50])

serie = pd.Series(arr, index=["a", "b", "c", "d", "e"])
print("Serie de Pandas:\n", serie)

# Salida:

Serie de Pandas:
a 10
b 20
c 30
d 40
e 50
dtype: int32
```

# Clase 31

Pandas:
```py
import pandas as pd

# Crear una Serie (columna de datos)
serie = pd.Series([10, 20, 30, 40, 50])
print("Serie:")
print(serie)

# Crear un DataFrame (tabla)
datos = {
"Nombre": ["Ana", "Luis", "Carla", "Pedro"],
"Edad": [23, 35, 29, 42],
"Ciudad": ["Córdoba", "Buenos Aires", "Rosario", "Mendoza"]
}
df = pd.DataFrame(datos)
print("\nDataFrame:")
print(df)
```

Salida esperada:

Serie:
0 10
1 20
2 30
3 40
4 50

dtype: int64

DataFrame: 
Nombre Edad Ciudad
0 Ana 23 Córdoba
1 Luis 35 Buenos Aires
2 Carla 29 Rosario
3 Pedro 42 Mendoza

Vemos que *Series* son como columnas individuales y **DataFrames** son tablas
completas. Estas dos estructuras son la base de todo lo que haremos con Pandas

Ahora, supongamos que no queremos que el indice sea 0 1 2 3 que se encuentra a la izquierda, para personalizar esto, podriamos utilizar la siguiente instrucción:
```py
# Serie a partir de una lista
serie = pd.Series([10, 20, 30, 40])
print("Serie desde lista:")
print(serie)

# Serie con índices personalizados
serie_idx = pd.Series([10, 20, 30, 40], index=["a", "b", "c", "d"])
print("\nSerie con índices personalizados:")
print(serie_idx)

# Serie a partir de un diccionario
serie_dict = pd.Series({"Ana": 23, "Luis": 35, "Carla": 29})
print("\nSerie desde diccionario:")
print(serie_dict)
```

Salida esperada:

Serie desde lista:
0 10
1 20
2 30
3 40

Serie con índices personalizados:
a 10
b 20
c 30
d 40

Serie desde diccionario:
Ana 23
Luis 35
Carla 29

¿Como tomamos esos datos?
**Indexación en Series**
```py
# Acceso por índice numérico
print(serie[0]) # 10

# Acceso por etiqueta
print(serie_idx["b"]) # 20

# Slicing (por posición)
print(serie[1:3]) # valores 20 y 30, va a imprimier el valor desde 1 hasta 3, pero sin incluir el 3, ya que no lo incluye

# Slicing (por etiquetas)
print(serie_idx["b":"d"]) # no rije un numero posicional, la posicion esta marcada por un criterio de recorrido que se basa en un principio de "Literalidad" por lo tanto si incluye la "d", por lo tanto devuelve: b, c y d
```

**Operaciones básicas con Series**:
```py
# Operaciones aritméticas
print(serie + 5) # suma 5 a todos los elementos
print(serie * 2) # multiplica por 2

# Comparaciones
print(serie > 25) # devuelve True/False por cada valor

# Funciones estadísticas
print("Suma:", serie.sum())
print("Media:", serie.mean())
print("Máximo:", serie.max())
```

Desde un diccionario de listas
```py
datos = {
"Nombre": ["Ana", "Luis", "Carla", "Pedro"],
"Edad": [23, 35, 29, 42],
"Ciudad": ["Córdoba", "Buenos Aires", "Rosario", "Mendoza"]
}
df = pd.DataFrame(datos)
print(df)
```
Salida esperada:
Nombre Edad Ciudad
0 Ana 23 Córdoba
1 Luis 35 Buenos Aires
2 Carla 29 Rosario
3 Pedro 42 Mendoza


## Serie

Entonces una serie es una columna individual con indicies

## Data frames

Es una tabla completa con filas y columnas

<><><><><><><><><><><><><><><><><><><><>
## Operaciones básicas con DataFrames

#### Ver primeras filas
print(df.head())

#### Seleccionar una columna
print(df["Nombre"])

#### Seleccionar varias columnas
print(df[["Nombre", "Edad"]])

#### Seleccionar una fila por índice
print(df.loc[0]) # por etiqueta
print(df.iloc[2]) # por posición

#### Estadísticas rápidas
print(df.describe())