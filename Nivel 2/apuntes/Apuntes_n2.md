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

