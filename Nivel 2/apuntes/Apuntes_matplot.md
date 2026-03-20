# Clase 38

## Introducción

Es una libreria estandar de python, creada para visualizar datos.

Seborn es otro programa de visualización, para utilizar seaborn se debe importar matplotlib, es una herramienta más "sencilla".

Ventajas de seaborn, tiene estilos "Más atractivos", tiene funciones especializadas en las funciones estadísticas, utiliza el metodo de maplot pltshow.

Otro programa de visualización es plotly. Este es más interactivo, selecionar graficos, es un grafico que no es una foto, es interactivo.


### Formatos

Matplot permite guardar las figuras en diferentes formatos, utilizando la funcion ```plt.savefig()```, por ejemplo
```py
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y)
plt.title("Grafico simple de ejemplo")

# Guardar como imagen PNG
plt.savefig("grafico.png")

# Guardar con mayor resolucion (300 dpi)
plt.savefig("grafico_hd.png", dpi=300)
```


Hay formas de agregar títulos o etiquetas y cambiar el diseño en matplot.
Utilizar ```plt.title``` y ```plt.label``` permite poner la referencia.

Para realizar el grafico de una forma mas atractiva hay comandos, estos pueden ser cosas como:

```py
plt.plot(meses, ventas, marker="o", color="blue", linestyle="--")
```

Dónde:
* marker="o" dibuja un círculo en cada punto.
* color="blue" define el color de la línea.
* linestyle="--" traza la línea con un estilo punteado.

### Objetos

Matplot consiste de dos objetos.
Las figuras, es el lienzo o contenedor general de un gráfico.Y los ejes o (axes) que representan cada gráfico con sus ejes x e y donde se dibujan los datos.

El siguiente ejemplo muestra la creación explícita de una figura y un eje:
```py
import matplotlib.pyplot as plt

# Crear figura y un eje
fig, ax = plt.subplots()

# Dibujar en el eje
ax.plot([1, 2, 3], [2, 4, 6])

# Titulos y etiquetas
ax.set_title("Ejemplo con Figure y Axes")
ax.set_xlabel("Eje X")
ax.set_ylabel("Eje Y")
plt.show()
```

# Clase 39

## Colores, estilos y marcadores

### Colores

Los colores se pueden definir por nombre como "red" o con el código hexadecimal "#FF5733" o escala de grises como "0.5", donde 0 es negro y 1 es blando.

Ejemplo: 
```py
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]

plt.plot(x, y1, color="blue", label="Linea Azul")
plt.plot(x, y2, color="#FF5733", label="Linea Naranja")
plt.legend()
plt.show()
```

### Estlos

Algunos estilos frecuentes son "-" (sólido), "--" (punteado), "-." (guiones y puntos) y ":" (puntos).

Ejemplo: 
```py
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]

plt.plot(x, y1, linestyle="--", color="green", label="Linea punteada")
plt.plot(x, y2, linestyle=":", color="purple", label="Linea de puntos")
plt.legend()
plt.show()
```

### Marcadores 
Los marcadores resaltan cada punto de la serie. Hay marcadores como "o" (círculo), "s" (cuadrado), "^" (triángulo) y "*" (estrella).

Ejemplo:
```py
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]

plt.plot(x, y1, marker="o", color="red", label="Con circulos")
plt.plot(x, y2, marker="s", color="blue", label="Con cuadrados")
plt.legend()
plt.show()
```

### Limites de ejes 

Podemos ajustar el rango de los ejes, esto permite destacar una región específica de datos o enfocar una zona de interes. Matplot nos permite invertir los ejes en el caso de que se requiera.

Ejemplo
```py
import matplotlib.pyplot as plt

# --- Limites --- #

x = [0, 1, 2, 3, 4, 5, 6]
y = [0, 1, 4, 9, 16, 25, 36]

plt.plot(x, y, marker="o")
plt.title("Ejemplo con limites de ejes")
plt.xlim(0, 6) # Limite para el eje X
plt.ylim(0, 40) # Limite para el eje Y
plt.show()

# --- Limites invertidos --- #

x = [0, 1, 2, 3, 4, 5, 6]
y = [0, 1, 4, 9, 16, 25, 36]

plt.plot(x, y, marker="o")
plt.title("Limites invertidos")
plt.xlim(6, 0) # Invierte el eje X
plt.ylim(40, 0) # Invierte el eje Y
plt.show()
```

### Leyendas, etiquetas y anotaciones

#### Leyendas
Las leyendas identifican cada serie del gráfico. Se define un label por serie y luego se llama a plt.legend().
Las leyendas mas comunes son "upper left" , "upper right" , "lower left" , "lower right" , "center" .

Ejemplo:
```py
x = [1, 2, 3, 4]
y1 = [1, 4, 9, 16]
y2 = [1, 2, 3, 4]

plt.plot(x, y1, label="Cuadrados")
plt.plot(x, y2, label="Lineal")
plt.legend(loc="upper left")
plt.title("Leyenda en la esquina superior izquierda")
plt.show()
```

#### Etiquetas en los ejes

Esto se puede ver directamente en el ejemplo

```py
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

plt.plot(x, y)
plt.xlabel("Valores de X")
plt.ylabel("Valores de Y")
plt.title("Ejemplo con etiquetas en los ejes")
plt.show()
```

#### Anotaciones

Resalta puntos específicos con texto y flechas que guían la atención.

Ejemplo:
```py
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y, marker="o")
plt.title("Anotacion de un punto clave")
plt.annotate(
    "Aqui esta 3",
    xy=(3, 9),
    xytext=(4, 12),
    arrowprops=dict(facecolor="black", shrink=0.05, width = 1) # Donde shrink es la distancia al texto y width el espesor de la flecha
)
plt.show()
```

## Tipos de gráficos básicos

### Gráficos de líneas

Utilizado para seguir la evolución de una variable en el tiempo o frente a otra magnitud.

Ejemplo: 
```py
# --- Datos --- #

meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun"]
ventas = [100, 120, 90, 140, 180, 160]

# --- Gráfico de líneas --- #

plt.plot(meses, ventas, marker="o", color="blue", linestyle="-") #plt.plot es linea

plt.title("Ventas mensuales")
plt.xlabel("Meses")
plt.ylabel("Ventas (en miles)")

plt.show()
```

### Diagrama de dispersión

Muestra la relación entre dos variables numéricas, detectando correlaciones o agrupamientos

```py
# --- Datos --- #
altura = [150, 160, 170, 180, 190, 200]
peso = [50, 60, 65, 80, 85, 95]

# --- Diagrama de dispersión --- #
plt.scatter(altura, peso, color="red", marker="x") # plt.scatter es de dispersión

plt.title("Relación entre altura y peso")
plt.xlabel("Altura (cm)")
plt.ylabel("Peso (kg)")

plt.show()
```

### Gráficos de barras 

Sirven para comparar categorías o valores discretos.

Puede ser de barras verticales o horizontales

Ejemplo vertical:
```py
# --- Datos --- #
categorias = ["A", "B", "C", "D"]
valores = [4, 7, 1, 8]

# --- Gráfico de barra --- #
plt.bar(categorias, valores, color="orange") # plt.bar es grafico de barra
plt.title("Gráfico de barras")
plt.xlabel("Categorías")
plt.ylabel("Valores")

plt.show()
```

Ejemplo horizontal:
```py
# --- Datos --- #
categorias = ["A", "B", "C", "D"]
valores = [4, 7, 1, 8]

# --- Gráfico de barra --- #
plt.barh(categorias, valores, color="green")
plt.title("Gráfico de barras horizontal")
plt.xlabel("Valores")
plt.ylabel("Categorías")
plt.show()
```

### Histogramas

Muestran la distribución de frecuencias de un conjunto de datos, agrupándolos en intervalos. 

Ejemplo: (utilizando python para generar datos para el ejemplo)
```py
import matplotlib.pyplot as plt
import numpy as np

# --- Generar datos aleatorios --- #
datos = np.random.randn(1000) # Distribución normal

# --- Grafico --- #
plt.hist(datos, bins=30, color="skyblue", edgecolor="black") # plt.hist es gráfico de histograma
plt.title("Histograma de distribución normal")
plt.xlabel("Valor")
plt.ylabel("Frecuencia")
plt.show()
```

### Boxplot o caja y bigote

Sintetiza la distribución de un conjunto de datos, la caja representa el rengo de variación, la línea central la media o mediana y los bigotes los valores extremos

Ejemplo:
```py
# --- Datos --- #
grupo1 = [7, 8, 5, 6, 9, 10, 6, 7, 8, 6]
grupo2 = [5, 6, 7, 8, 7, 9, 5, 6, 6, 7]

# --- Gráfico de caja y bigote --- #
plt.boxplot([grupo1, grupo2], tick_labels=["Grupo 1", "Grupo 2"]) # plt.boxplot es caja y bigote.
plt.title("Comparación de dos grupos")
plt.ylabel("Valores")
plt.show()
```

## Graficos avanzados

La diferencia con los graficos anteriores es que estos no forman parte directa de matplot, se debe decirle a matplot como es el grafico y como hacerlo, por eso se usa con objetos.

### Gráfico de torta

Los gráficos de torta muestran proporciones de un total. 

* Utilizá Axes.pie para crear el gráfico desde un objeto Axes.
* Mantené la relación de aspecto en 1:1 con ax.set_aspect('equal') para obtener un círculo.
* autopct muestra porcentajes formateados.
* explode resalta sectores relevantes.
* labels o ax.legend() facilitan la lectura.

Ejemplo: 

```py
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

valores = [40, 25, 20, 15] # Deben ser = al 100%
labels = ["Ventas", "Marketing", "I+D", "Operaciones"]
explode = [0.05, 0, 0, 0] # Resaltar "Ventas"

ax.pie(
    valores,
    labels=labels,
    explode=explode,
    autopct="%.1f%%", # autopct es el formato del porcentaje, ahi dice que solo va a tener un decimal
    startangle=90,
    wedgeprops={"linewidth": 1, "edgecolor": "white"}
)

ax.set_title("Distribución de presupuesto")
ax.set_aspect('equal') # Círculo perfecto
plt.show()
``` 

### Gráfico de área (fill_between)

Estos gráficos destacan el área bajo una curva o entre dos curvas.

#### Para un área bajo una curva

```py
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 200)
y = np.sin(x) + 1.5

fig, ax = plt.subplots()
ax.plot(x, y, label="Señal")
ax.fill_between(x, y, 0, alpha=0.3) # Relleno hasta el eje X

ax.set_title("Área bajo la curva")
ax.set_xlabel("Tiempo")
ax.set_ylabel("Amplitud")
ax.legend()
plt.show()
```

Gráfico entre dos curvas

```py
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 300)
y1 = np.sin(x) + 1
y2 = np.cos(x) + 1

fig, ax = plt.subplots()
ax.plot(x, y1, label="Seno")
ax.plot(x, y2, label="Coseno")
ax.fill_between(x, y1, y2, where=(y1 >= y2), alpha=0.25, label="Área (y1 >= y2)")
ax.fill_between(x, y1, y2, where=(y1 < y2), alpha=0.25, label="Área (y1 < y2)")

ax.set_title("Área entre dos curvas")
ax.set_xlabel("Ángulo")
ax.set_ylabel("Valor")
ax.legend()
plt.show()
```

#### Grafico de densidad (density=True) con histograma

Para analizar distribuciones

```py
import numpy as np

np.random.seed(42)
muestras = np.random.normal(loc=0, scale=1, size=2000)
fig, ax = plt.subplots()

# Histograma como densidad
ax.hist(
    muestras,
    bins="auto",
    density=True, # Esto es lo que cambia en relación a un histograma normal
    edgecolor="black",
    alpha=0.4,
    label="Hist (densidad)"
)

# Curva normal estimada con media y desvío de los datos
mu, sigma = np.mean(muestras), np.std(muestras, ddof=1)
x = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 400)
pdf = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)
ax.plot(x, pdf, linewidth=2, label=f"N(mu={mu:.2f}, sigma={sigma:.2f})")

ax.set_title("Distribución y densidad (hist con density=True)")
ax.set_xlabel("Valor")
ax.set_ylabel("Densidad")
ax.legend()
plt.show()
```

# Clase 40

## Graficos avanzados

### Diagramas de error

Las barras de error muestran incertidumbre en mediciones. Podés combinar errores verticales (yerr) y horizontales (xerr) y ajustar tapas (capsize). Este gráfico  cuantifica la dispersión de las mediciones, estima la incertidumbre de la media y indica el rango probable del valor real con un 95% de confianza.

#### Errores vertivales

```py
import numpy as np

x = np.arange(1, 6)
y = np.array([2.0, 2.5, 3.7, 3.2, 4.1])
yerr = np.array([0.2, 0.3, 0.25, 0.35, 0.2]) # Error vertical

fig, ax = plt.subplots()

ax.errorbar(
    x,
    y,
    yerr=yerr,
    fmt="o-", # Marcador + línea
    capsize=4, # Tapa de las barras de error
    elinewidth=1.2, # Grosor de la barra de error
    label="Medición con error"
)

ax.set_title("Diagrama de error (errorbar)")
ax.set_xlabel("Muestra")
ax.set_ylabel("Valor medido")
ax.legend()
plt.show()
```


#### Errore en x e y

```py
import numpy as np

x = np.linspace(0.5, 2.5, 5)
y = np.array([1.5, 1.8, 2.1, 2.0, 2.3])
xerr = 0.1
yerr = [0.05, 0.1, 0.08, 0.12, 0.06]

fig, ax = plt.subplots()
ax.errorbar(
    x,
    y,
    xerr=xerr,
    yerr=yerr,
    fmt="s--",
    capsize=3,
    ecolor="gray",
    label="Error en X e Y"
)

ax.set_title("Barras de error en ambos ejes")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.legend()
plt.show()
```

## Subplots y figuras múltiples

### Uso de subplot y subplots
plt.subplot sigue el estilo imperativo clásico, mientras que plt.subplots devuelve la pareja (fig, ax) y simplifica el trabajo con la API moderna.

Veamos esto con un ejemplo básico.
```py
import numpy as np

x = np.linspace(0, 2 * np.pi, 200)

# Sintaxis moderna: Figure y arreglo de Axes
fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(8, 6), layout='constrained')
# 'layout="constrained"' ayuda a evitar solapamientos de textos y etiquetas.

# Función 1
axs[0, 0].plot(x, np.sin(x)) # con axs[m,n] determinamos la posicion del gráfico, con lo que sigue, determinamos el grafico en sí
axs[0, 0].set_title("sin(x)")

# Función 2
axs[0, 1].plot(x, np.cos(x), linestyle="--")
axs[0, 1].set_title("cos(x)")

# Función 3
axs[1, 0].plot(x, np.tan(x))
axs[1, 0].set_title("tan(x)")
axs[1, 0].set_ylim(-3, 3) # Acotar tan(x)

# Función 4
axs[1, 1].plot(x, np.sin(x) * np.cos(x), marker="o", markersize=2, linestyle="-")
axs[1, 1].set_title("sin(x)*cos(x)")

fig.suptitle("Cuadrícula 2x2 con subplots", fontsize=12)
plt.show()
```
layout='constrained' (o constrained_layout=True) es para que Matplotlib gestione los márgenes.
* fig, ax = plt.subplots() devuelve un arreglo de Axes cuando nrows *ncols > 1.
* Usá axes.flat para iterar sobre todos los subplots con un solo bucle


### Gráficos que compartan ejes
Compartir ejes sincroniza límites, ticks y zoom/pan entre subplots, ideal para comparaciones en la misma escala.

Para compartir eje x se utiliza sharex=true, veamos el ejemplo:
```py
import numpy as np

t = np.linspace(0, 10, 500)
s1 = np.sin(t)
s2 = np.cos(t)

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(8, 5), layout='constrained') # aquí colocamos sharex

ax1.plot(t, s1, label="sin(t)")
ax1.set_ylabel("Amplitud")
ax1.legend()

ax2.plot(t, s2, color="orange", label="cos(t)")
ax2.set_xlabel("Tiempo")
ax2.set_ylabel("Amplitud")
ax2.legend()

fig.suptitle("Subplots compartiendo eje X")
plt.show()
```

Para compartir eje Y:
```py
import numpy as np

x = np.linspace(0, 5, 200)
fig, (ax1, ax2) = plt.subplots(1, 2, sharey=True, figsize=(9, 4), layout='constrained')

ax1.plot(x, np.exp(x))
ax1.set_title("exp(x)")
ax1.set_xlabel("x")
ax1.set_ylabel("y")

ax2.plot(x, np.exp(0.5 * x))
ax2.set_title("exp(0.5x)")
ax2.set_xlabel("x")

fig.suptitle("Subplots compartiendo eje Y")
plt.show()
```


### Diseño avanzado con ``Grid Spec``

Permite composiciones flexibles, celdas de distintos tamaños, subplots que abarcan varias filas/columnas y control de proporciones.

Conceptos clave
* Definí la grilla con ``GridSpec(nrows, ncols)``.
* Creá ejes con ``fig.add_subplot(gs[fila_ini:fila_fin,col_ini:col_fin])``.
* Usá width_ratios y height_ratios para ajustar proporciones.

veamos un ejemplo
```py
import numpy as np
from matplotlib.gridspec import GridSpec

x = np.linspace(0, 2 * np.pi, 300)

fig = plt.figure(figsize=(9, 6), layout='constrained')

gs = GridSpec(nrows=2, ncols=2, figure=fig, height_ratios=[2, 1])

ax_top = fig.add_subplot(gs[0, :]) # Este es el gráfico, los : sin nada, significa que va a tomar todos los parámetros, ya que no hay parametro final
ax_top.plot(x, np.sin(x), label="sin(x)")
ax_top.plot(x, np.cos(x), label="cos(x)")
ax_top.set_title("Superior: sin y cos")
ax_top.legend()

ax_bl = fig.add_subplot(gs[1, 0]) # Este es el grafico
ax_bl.plot(x, np.sin(2 * x), color="purple")
ax_bl.set_title("Inferior Izq: sin(2x)")

ax_br = fig.add_subplot(gs[1, 1])
ax_br.plot(x, np.cos(2 * x), color="green")
ax_br.set_title("Inferior Der: cos(2x)")

fig.suptitle("Diseño avanzado con GridSpec (1 grande arriba, 2 abajo)")
plt.show()
```

### Estilos y temas

cómo aplicar estilos predefinidos, ajustar tipografías y fondos mediante rcParams

ejemplo

```py
import numpy as np

print(plt.style.available) # Lista de estilos disponibles
plt.style.use("seaborn-v0_8") # Aplica estilo global hasta cambiarlo

x = np.linspace(0, 2 * np.pi, 200)
y = np.sin(x)

fig, ax = plt.subplots(layout="constrained")

ax.plot(x, y, label="sin(x)")
ax.set_title("Ejemplo con estilo 'seaborn-v0_8'")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()
plt.show()
```


#### Cambiar tipogrfías y tmeas

Las preferencias visuales se controlan de forma global con mpl.rcParams o de manera localizada sobre cada figura y eje.

```py
import matplotlib as mpl
import numpy as np

mpl.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 11,
    "figure.facecolor": "#FFFFFF",
    "axes.facecolor": "#FAFAFA",
    "axes.edgecolor": "#333333",
    "axes.grid": True,
    "grid.linestyle": "--",
    "grid.alpha": 0.4,
    "axes.titlesize": 13,
    "axes.labelsize": 11,
    "legend.frameon": False,
})

x = np.linspace(0, 10, 200)
y = np.exp(-0.2 * x) * np.sin(3 * x)

fig, ax = plt.subplots(layout="constrained")

ax.plot(x, y, marker="o", markersize=3)
ax.set_title("Fuente, grilla y fondos personalizados (global)")
ax.set_xlabel("Tiempo")
ax.set_ylabel("Amplitud")
plt.show()
```

## Graficar de pandas y numpy

Cuando trabajás con datos tabulares, Pandas y NumPy se integran de manera natural con Matplotlib. Podés graficar directamente desde DataFrames, preparar series temporales y realizar cálculos vectorizados con NumPy sin perder la API orientada a objetos de Matplotlib.


# Clase 41

#### Ejemplo con titanic
Cargamos el dataset Titanic desde Seaborn, lo convertimos en un DataFrame de Pandas y generamos gráficos con Matplotlib manteniendo la API orientada a objetos.

```py
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# 1) Cargar y preparar datos
Titanic = sns.load_dataset("titanic")
Titanic = Titanic[["survived", "class", "sex", "age", "fare"]].dropna()

# 2) Tasa de supervivencia por clase y sexo
fig, ax = plt.subplots(layout="constrained")
survival_rate = Titanic.groupby(["class", "sex"])["survived"].mean().unstack()
survival_rate.plot(kind="bar", ax=ax)
ax.set_title("Titanic: Supervivencia por clase y sexo")
ax.set_xlabel("Clase")
ax.set_ylabel("Tasa de supervivencia")
ax.legend(title="Sexo")
plt.show()

# 3) Dispersión: edad vs. tarifa (fare)
fig, ax = plt.subplots(figsize=(7, 5), layout="constrained")
ax.scatter(Titanic["age"], Titanic["fare"], c=Titanic["survived"],  # Es el grafico de dispersión.
cmap="coolwarm", alpha=0.7)
ax.set_title("Titanic: Edad vs. Tarifa")
ax.set_xlabel("Edad")
ax.set_ylabel("Tarifa")
plt.show()

# 4) Histogramas de edad por supervivencia
fig, ax = plt.subplots(figsize=(7, 4), layout="constrained")
for survived, subset in Titanic.groupby("survived"):
etiqueta = "Sobrevive" if survived == 1 else "No sobrevive"
ax.hist(subset["age"], bins="auto", alpha=0.5, density=True, label=etiqueta)
ax.set_title("Titanic: Densidad de edad por supervivencia")
ax.set_xlabel("Edad")
ax.set_ylabel("Densidad")
ax.legend()
plt.show()
```

## Visualización de series temporales

Las series temporales son omnipresentes en análisis financiero, monitoreo de sensores y planificación. Pandas y NumPy se integran con Matplotlib para convertir fechas, formatear ejes y resamplear tendencias.

### conversion de fechas con pd.to_datetime
Casos típicos: columnas de texto a datetime64[ns], detección automática o manual de formatos, manejo de valores inválidos (errors="coerce") y zonas horarias (tz_localize, tz_convert).

```py
import pandas as pd

df = pd.DataFrame({
    "fecha": ["2025-01-01", "2025-01-02", "01/03/2025", "2025/01/04", "2025-13-01"],
    "valor": [10, 12, 11, 15, 14]
})

df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce", dayfirst=False)
# df["fecha"] = pd.to_datetime(df["fecha"], format="%Y-%m-%d") # Formato explícito
df = df.set_index("fecha").sort_index()
# df = df.tz_localize("UTC").tz_convert("America/Argentina/Cordoba")
```
unificá la zona horaria, ordená con df.sort_index() y documentá la política de datos faltantes.

### Gráficos de series de tiempos
#### Línea básica con matplotlib (API OO)
```py
import pandas as pd

df = pd.DataFrame({
    "fecha": ["2025-01-01", "2025-01-02", "01/03/2025", "2025/01/04", "2025-13-01"],
    "valor": [10, 12, 11, 15, 14]
})

df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce", dayfirst=False)

# df["fecha"] = pd.to_datetime(df["fecha"], format="%Y-%m-%d") # Formato explicito

df = df.set_index("fecha").sort_index()

# df = df.tz_localize("UTC").tz_convert("America/Argentina/Cordoba")

fig, ax = plt.subplots(figsize=(8, 4), layout="constrained")
ax.plot(df.index, df["valor"], marker="o")
ax.set_title("Serie de tiempo: valor diario")
ax.set_xlabel("Fecha")
ax.set_ylabel("Valor")
plt.show()
```

### Resampleo y tendencias
Resamplear cambia la frecuencia temporal (por ejemplo, diario a semanal/mensual) con una agregación. Las tendencias se observan con ventanas móviles, medianas o suavizados exponenciales.
#### Resampleo a semanal/mensual
semana = df["valor"].resample("W").mean()
mes = df["valor"].resample("M").sum()

#### Ventanas móviles (rolling)
media7 = df["valor"].rolling(window=7, center=True, min_periods=1).mean()
mediana7 = df["valor"].rolling(7, center=True, min_periods=1).median()

#### Suavizado exponencial (EWM)
ewm14 = df["valor"].ewm(span=14, adjust=False).mean()

#### Tendencia integradora
```py
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(9, 4), layout="constrained")
ax.plot(df.index, df["valor"], alpha=0.4, label="Diario")
ax.plot(semana.index, semana, linewidth=2, label="Semanal (mean)")
ax.plot(media7.index, media7, linewidth=2, label="Media móvil 7D")
ax.plot(ewm14.index, ewm14, linewidth=2, label="EWM 14")
ax.set_title("Resampleo y tendencias")
ax.set_xlabel("Fecha")
ax.set_ylabel("Valor")
ax.legend()
plt.show()
```

#### Resampleo mensual y suavizado
```py
mensual_mean = df["valor"].resample("M").mean()
mensual_mean_3 = mensual_mean.rolling(3, min_periods=1).mean()
fig, ax = plt.subplots(figsize=(8, 4), layout="constrained")
ax.plot(mensual_mean.index, mensual_mean, marker="o", label="Mensual (mean)")
ax.plot(mensual_mean_3.index, mensual_mean_3, label="Mensual suavizada (3M)")
ax.set_title("Promedio mensual y suavizado 3 meses")
ax.set_ylabel("Valor")
ax.legend()
plt.show()
```

## Visualización 3d
Matplotlib ofrece soporte para gráficos 3D mediante `subplot_kw={"projection": "3d"}`. Con NumPy generamos datos y desde Matplotlib los visualizamos con dispersión, superficies y triangulaciones.

### importacion de mpl_toolkits.mplot3d

Desde Matplotlib moderno basta con crear el subplot con proyección 3D, sin importar Axes3D explícitamente.
```py
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(subplot_kw={"projection": "3d"}, figsize=(7, 5),
layout="constrained")

t = np.linspace(0, 2 * np.pi, 200)
x, y, z = np.cos(t), np.sin(t), t

ax.plot3D(x, y, z)
ax.set_title("Ejemplo 3D: hélice simple")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()
```

### Grafico de dispersión 3d
```py
import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(42)
n = 600
x = rng.normal(0, 1, n)
y = rng.normal(0, 1, n)
z = rng.normal(0, 1, n)
c = np.sqrt(x**2 + y**2 + z**2)

fig, ax = plt.subplots(subplot_kw={"projection": "3d"}, figsize=(7, 5), layout="constrained")
sc = ax.scatter(x, y, z, c=c, cmap="viridis", s=10, alpha=0.9)

ax.set_title("Dispersión 3D con color por distancia radial")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

cb = fig.colorbar(sc, ax=ax, shrink=0.7, pad=0.05)
cb.set_label("Distancia radial")
ax.set_box_aspect((1, 1, 1))
plt.show()
```
Se recomienda usar alpha moderado y set_box_aspect para evitar distorsiones.

#### Superficie en malla regular
```py
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 200)
y = np.linspace(-3, 3, 200)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

fig, ax = plt.subplots(subplot_kw={"projection": "3d"}, figsize=(7, 5), layout="constrained")

surf = ax.plot_surface(X, Y, Z, cmap="viridis", rstride=1, cstride=1, linewidth=0, antialiased=True) # cmap es el tipo de convinacion de colores.

ax.set_title("Superficie 3D: z = sin(sqrt(x^2 + y^2))")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

cb = fig.colorbar(surf, ax=ax, shrink=0.7, pad=0.05)
cb.set_label("Altura (Z)")
ax.view_init(elev=25, azim=45)
ax.set_box_aspect((1, 1, 0.5))
plt.show()

```

# Clase 42
## Visualización 3D

#### Superficie con datos dispersos (ax.plot_trisurf)
```py
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.tri import Triangulation

rng = np.random.default_rng(0)
n = 800
x = 6 * rng.random(n) - 3
y = 6 * rng.random(n) - 3
z = np.sin(np.sqrt(x**2 + y**2))

tri = Triangulation(x, y)

fig, ax = plt.subplots(subplot_kw={"projection": "3d"}, figsize=(7, 5), layout="constrained")
surf = ax.plot_trisurf(tri, z, cmap="plasma", linewidth=0.2, antialiased=True) # Cmap plasma es la convinación de colores llamado plasma.

ax.set_title("Superficie 3D triangulada (datos dispersos)")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

fig.colorbar(surf, ax=ax, shrink=0.7, pad=0.05).set_label("Altura (Z)")
ax.set_box_aspect((1, 1, 0.6))

plt.show()
```

#### Variantes
```py
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(subplot_kw={"projection": "3d"}, layout="constrained")
X, Y = np.meshgrid(np.linspace(-2, 2, 50), np.linspace(-2, 2, 50))
Z = np.cos(X) * np.sin(Y)
ax.plot_wireframe(X, Y, Z, rstride=2, cstride=2)
ax.set_title("Wireframe 3D")
plt.show()

fig, ax = plt.subplots(subplot_kw={"projection": "3d"}, layout="constrained")
ax.contour3D(X, Y, Z, levels=25, cmap="viridis")
ax.set_title("Contornos 3D")
plt.show()

from matplotlib.colors import LightSource

fig, ax = plt.subplots(subplot_kw={"projection": "3d"}, layout="constrained")
ls = LightSource(azdeg=315, altdeg=45)
rgb = ls.shade(Z, cmap=plt.get_cmap("terrain"), vert_exag=1.0,
blend_mode="soft")
ax.plot_surface(X, Y, Z, facecolors=rgb, linewidth=0, antialiased=False)
ax.set_title("Superficie con sombreado (LightSource)")
plt.show()
```

# Clase 43
## Interactividad en matplotlib
Matplot permite crear graficos interactivos, es uno que actualiza la figura a medida que va interactuando. Se ejecuta en terminal

### plt.ion() y graficos interactivos
La ventana de la figura procese eventos de zoom/pan sin bloquear tu código.
```py
import numpy as np
import matplotlib.pyplot as plt
import time

plt.ion()
fig, ax = plt.subplots(layout="constrained")

x = np.linspace(0, 2 * np.pi, 300)

(line,) = ax.plot(x, np.sin(x), label="sin(x)")
ax.set_ylim(-1.5, 1.5)
ax.legend()
fig.canvas.draw_idle() # Esto es lo que refresca y re dibuja el grafico, es lo que le da soporte al movimiento

for f in np.linspace(1, 3, 30):
    y = np.sin(f * x)
    line.set_ydata(y)
    ax.set_title(f"Frecuencia: {f:.2f} Hz") # .2f son 2 decimales flotantes, es el limite del float.
    fig.canvas.draw_idle()
    fig.canvas.flush_events()
    time.sleep(0.05) 

plt.ioff()
plt.show()
```

### Zoom, pan y selección
Matplotlib dispone de SpanSelector, RectangleSelector, LassoSelector, etc.

#### Selección horizontal con SpanSelector
```py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import SpanSelector

x = np.linspace(0, 10, 500)
y = np.sin(2 * np.pi * x) * np.exp(-0.2 * x)

fig, (ax, ax_zoom) = plt.subplots(2, 1, figsize=(8, 6), layout="constrained")
ax.plot(x, y)
ax.set_title("Arrastrá para seleccionar un rango (horizontal)")
ax_zoom.set_title("Zoom del rango seleccionado")

def onselect(xmin, xmax):
    mask = (x >= xmin) & (x <= xmax)
    ax_zoom.clear()
    ax_zoom.plot(x[mask], y[mask])
    ax_zoom.set_title(f"Rango seleccionado: {xmin:.2f} a {xmax:.2f}") # Esto va a marcar que valores seleccionamos en el zoom
    fig.canvas.draw_idle()

span = SpanSelector( # Es lo que estoy importando
        ax,
        onselect,
        direction="horizontal",
        useblit=True, # Es la forma de seleccionar un punto de interes, es el movimiento que damos cuando seleccionamos.
        props=dict(alpha=0.3), # Es la transparencia del rango de selección.
        interactive=True
    )

plt.show()
```

#### Selección rectangular con RectangleSelector
```py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import RectangleSelector

rng = np.random.default_rng(0)
x = rng.normal(0, 1, 800)
y = rng.normal(0, 1, 800)

fig, ax = plt.subplots(layout="constrained")
pts = ax.scatter(x, y, s=12, alpha=0.7)

ax.set_title("Arrastrá un rectángulo para seleccionar puntos")

def onselect(eclick, erelease):
    xmin, xmax = sorted([eclick.xdata, erelease.xdata])
    ymin, ymax = sorted([eclick.ydata, erelease.ydata])
    sel = (x >= xmin) & (x <= xmax) & (y >= ymin) & (y <= ymax)
    pts.set_alpha(np.where(sel, 1.0, 0.3))
    fig.canvas.draw_idle()

rect = RectangleSelector(
    ax,
    onselect,
    useblit=True,
    button=[1],
    props=dict(facecolor="tab:blue", alpha=0.15, edgecolor="k")
    )
    
plt.show()
```

## Widgets básicos (Slider, RangeSlider, Button)
Permiten agregar controles sencillos dentro de la figura

### Slider para controlar parámetros
```py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

x = np.linspace(0, 2 * np.pi, 400) # Crea 400 puntos entre 0 y 2π para que la curva se vea suave.
fig, ax = plt.subplots(figsize=(8, 5), layout="constrained") 
(line,) = ax.plot(x, np.sin(1 * x), label="sin(freq*x)") # devuelve una lista de objetos; al usar la coma, extraemos el primer objeto (la línea de la gráfica) para poder modificar sus datos más tarde en la función de actualización.
ax.set_ylim(-1.5, 1.5)
ax.legend()

# Creación del slider
ax_slider = fig.add_axes([0.15, 0.05, 0.7, 0.04])
slider_freq = Slider(ax=ax_slider, label="Frecuencia", valmin=0.5, valmax=5.0, valinit=1.0) # valinit: La gráfica empieza con una frecuencia de 1.0.

def actualizar(val):
    f = slider_freq.val
    line.set_ydata(np.sin(f * x)) # En lugar de borrar y crear una gráfica nueva (que sería lento), solo cambia los valores de la y en la línea existente.
    ax.set_title(f"f = {f:.2f}")
    fig.canvas.draw_idle()

slider_freq.on_changed(actualizar) # Esta línea conecta el movimiento del slider con la función actualizar
plt.show()
```

### RangeSlider para definir interval
```py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import RangeSlider

x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x) + 0.2 * np.sin(10 * x)

fig, ax = plt.subplots(figsize=(8, 5), layout="constrained")
(line,) = ax.plot(x, y)
ax.set_ylim(-2, 2)

ax_r = fig.add_axes([0.15, 0.05, 0.7, 0.04])
rs = RangeSlider(
    ax=ax_r,
    label="Rango X",
    valmin=float(x.min()),
    valmax=float(x.max()),
    valinit=(float(x.min()), float(x.max()))
    )

def actualizar_rango(val):
    xmin, xmax = rs.val
    ax.set_xlim(xmin, xmax)
    fig.canvas.draw_idle()

rs.on_changed(actualizar_rango)
plt.show()
```

### Botón para resetear o lanzar acciones
```py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

x = np.linspace(0, 2 * np.pi, 400)
fig, ax = plt.subplots(figsize=(8, 5), layout="constrained")
(line,) = ax.plot(x, np.sin(1 * x))
ax.set_ylim(-1.5, 1.5)

ax_s = fig.add_axes([0.15, 0.05, 0.6, 0.04])
sl = Slider(ax=ax_s, label="Frecuencia", valmin=0.5, valmax=5.0, valinit=1.0)

def on_change(val):
    line.set_ydata(np.sin(sl.val * x))
    fig.canvas.draw_idle()

sl.on_changed(on_change)

ax_b = fig.add_axes([0.78, 0.05, 0.12, 0.04])
btn = Button(ax=ax_b, label="Reset")

def on_reset(event):
    sl.reset()

btn.on_clicked(on_reset)
plt.show()
```

## Animaciones
FuncAnimation de Matplotlib permite animar artistas (líneas, scatter, textos) actualizando su estado en cada frame.

* fig: figura a animar.
* func(i): actualiza artistas y retorna una lista/tupla de objetos.
* init_func(): estado inicial (opcional, necesario para blitting).
* frames: número de frames o iterador.
* interval: milisegundos entre frames.
* blit=True: redibuja solo lo que cambia.

### Animacion de una onda sinusoidal
#### Onda viajera
```py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x = np.linspace(0, 2 * np.pi, 600)
fig, ax = plt.subplots(figsize=(7, 4), layout="constrained")
(line,) = ax.plot(x, np.sin(x))
ax.set_xlim(x.min(), x.max())
ax.set_ylim(-1.2, 1.2)
ax.set_title("Onda sinusoidal animada")
ax.set_xlabel("x")
ax.set_ylabel("y = sin(x - fase)")

def init():
    line.set_ydata(np.sin(x))
    return (line,)

def update(frame):
    fase = 0.05 * frame
    line.set_ydata(np.sin(x - fase))
    return (line,)

ani = FuncAnimation(
    fig,
    update,
    frames=200,
    init_func=init,
    interval=20,
    blit=True,
    repeat=True
    )

plt.show()
```

### Guardar animaciones en GIF o MP4

#### Guardar como GIF
```py
from matplotlib.animation import PillowWriter

# ani = FuncAnimation(...)
writer = PillowWriter(fps=30)
ani.save("onda.gif", writer=writer, dpi=100)
```
#### Guardar como MP4
```py
from matplotlib.animation import FFMpegWriter
# ani = FuncAnimation(...)
writer = FFMpegWriter(fps=30, bitrate=1800)
ani.save("onda.mp4", writer=writer, dpi=120)
```
Necesita FFmpeg, se debe instalar por consola.

## Exportación y publicación de gráficos

### Guardar en diferentes formatos
```py 
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x)

fig, ax = plt.subplots(figsize=(6, 4), layout="constrained")
ax.plot(x, y, label="sin(x)")
ax.set_title("Ejemplo de exportación")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()

fig.savefig("grafico.png", dpi=200, bbox_inches="tight")
fig.savefig("grafico.pdf", bbox_inches="tight")
fig.savefig("grafico.svg", bbox_inches="tight")
```

### Resolución
* Web: 96-150 dpi.
* Presentaciones: 150-200 dpi.
* Publicaciones impresas: 300-600 dpi.
```py
fig, ax = plt.subplots(figsize=(6, 4), layout="constrained")
fig.savefig("articulo.png", dpi=300)
```
### Preparación para artículos y presentaciones
```py
import matplotlib as mpl
from cycler import cycler

mpl.rcParams.update({
        "font.family": "DejaVu Sans",
        "font.size": 10,
        "axes.titlesize": 12,
        "axes.labelsize": 10,
        "legend.fontsize": 9,
        "xtick.labelsize": 9,
        "ytick.labelsize": 9,
        "lines.linewidth": 1.6,
        "lines.markersize": 4.0,
        "axes.grid": True,
        "grid.linestyle": "--",
        "grid.alpha": 0.35,
        "axes.prop_cycle": cycler(color=[
            "#1f77b4", "#ff7f0e", "#2ca02c", "#d62728",
            "#9467bd", "#8c564b", "#e377c2", "#7f7f7f"
            ])
    })

mpl.rcParams["pdf.fonttype"] = 42
mpl.rcParams["ps.fonttype"] = 42
mpl.rcParams["svg.fonttype"] = "none"
```
Mantén jerarquía tipográfica, alto contraste y paletas accesibles. Para LaTeX, activá `text.usetex` si la revista lo requiere