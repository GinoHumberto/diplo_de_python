# Clase 44 
## Introducción a seaborn

Es una libreria de visualización estadística. Esta realizada para trabajar directamente con data frames de pandas. 

La ventaja de Seaborn es que facilita crear fraficos informativos y elegantes con menos código.

¿Pero entonces porqué utilizariamos seaborn en ves matplotlib puro? 
* API de alto nivel: funciones como displot , catplot , relplot , heatmap y pairplot resuelven de una vez tareas que en Matplotlib requieren muchos pasos.
* Semántica declarativa: parámetros como hue , style , size , col y row conectan columnas del DataFrame con la estética visual sin código extra.
* Estilos y paletas predefinidos: mejoran la legibilidad y evitan invertir tiempo en configuración manual.
* Integración natural con Pandas: pasás el DataFrame y los nombres de las columnas sin separar manualmente series x e y.
* Objetos modernos (Seaborn Objects ≥ 0.13): una gramática coherente para combinar capas y construir composiciones avanzadas, similar a ggplot.

## ejemplo
Hay datasets que seaborn trae incorporados, por ejemplo "Tips".
```py
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips") # DataFrame con datos de propinas, tips es la variable y con sns.load_dataset traemos el data set de seaborn
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time", style="sex") # hue señala la categoria especifica, es como un marcador de matplot
plt.title("Relacion total de la cuenta vs propina")
plt.show()
```

### API de figura a nivel alto: grillas y facetas
Las funciones de nivel figura ( displot , catplot , relplot , lmplot ) crean figuras completas y facetas automáticamente
```py 
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
sns.displot(data=tips, x="total_bill", hue="time", kind="kde", fill=True, col="sex") # Displot es un tipo de faceta y kde es el grafico de distribución.
plt.show()
```

## Gramatica para construir con objetos
Una gramática unificada para construir gráficos por capas:
```py
import seaborn as sns
import seaborn.objects as so

tips = sns.load_dataset("tips")

(
    so.Plot(tips, x="total_bill", y="tip", color="time") # So.plot determino el tipo de linea
        .add(so.Dots(alpha=0.7)) # add(so.dots...) determina los puntos
         .add(so.Line(), so.PolyFit(order=1)) # So.line es la linea que conecta los puntos, Polyfit es la regresion. Order es el grado del polinomio que utiliza para la regresión. Si queremos que el polinomio sea grado 10 order = 10 (que seria f(x)=x^10 + x^9 + ... )
        .theme(sns.plotting_context("notebook"))
).show()
```

## Estilos y colores predefinidos:
Seaborn incluye estilos coherentes para fondos, rejillas y ticks:
* darkgrid (por defecto tradicional)
* whitegrid (ideal para datos categóricos)
* dark
* white
* ticks
Aplicación:
```py
sns.set_theme(style="whitegrid") # "darkgrid", "white", "dark" o "ticks"
```

## Etiquetas, titulos y ticks
Se elige el estilo con `context`
* paper
* notebook (default)
* talk
* poster
```py
sns.set_theme(context="talk") # Ideal para presentaciones
```

## Paletas de color
* Cualitativas: "deep" , "muted" , "bright" , "pastel" , "dark" , "colorblind" .
* Secuenciales: "rocket" , "mako" , "flare" , "crest" , "viridis" , "magma" , entre otras.
* Divergentes: "vlag" , "icefire" , "coolwarm" , "Spectral" .

### Aplicación global o local:

#### Global: todos los graficos siguientes
```py
sns.set_palette("deep") # O cualquier nombre de paleta
```
#### Local: solo para un grafico
```py
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time", palette="Set2")
```

## Combinar Seaborn con Matplotlib

```py
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
sns.boxplot(data=tips, x="day", y="total_bill", hue="smoker", palette="pastel")
plt.title("Cuenta total por dia y habito de fumar")
plt.xlabel("Dia de la semana")
plt.ylabel("Total de la cuenta (USD)")
plt.legend(title="Fumador")
plt.show()
```


# Clase 45

## Histograma con histplot:

```py
import seaborn as sns
import matplotlib.pyplot as plt

# Tema visual recomendado
sns.set_theme(style="whitegrid", context="notebook")

# Dataset de ejemplo
tips = sns.load_dataset("tips")

# Histograma simple de la cuenta total
sns.histplot(data=tips, x="total_bill")
plt.title("Histograma de total_bill (cuenta total)")
plt.xlabel("Total de la cuenta (USD)")
plt.ylabel("Frecuencia")
plt.show()
```


## Variables categóricas con hue y múltiples series

El parámetro hue colorea por categoría y multiple define cómo se combinan las series.
```py
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid", context="notebook")
tips = sns.load_dataset("tips")
sns.histplot(
    data=tips,
    x="total_bill",
    hue="time", # Lunch vs Dinner
    element="bars",
    multiple="stack", # layer | stack | dodge | fill
    bins=25,
    stat="count"
)
plt.title("Histograma por momento del día (stack)")
plt.show()
```


## Distribuciones discretas (enteros)
Para datos enteros (por ejemplo, cantidad de comensales) indicá discrete=True o definí binwidth=1 .
```py 
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid", context="notebook")
tips = sns.load_dataset("tips")

sns.histplot(
    data=tips,
    x="size", 
    discrete=True, # tamaño de grupo (entero) No existe 1 persona y media, solo existe una 
    shrink=0.9 # Deja espacio entre barras
)

plt.title("Histograma de tamaño de grupo (discreto)")
plt.xlabel("Tamaño de grupo")
plt.ylabel("Frecuencia")
plt.show()
```


## KDE (kernel density estimation) Básico

Es una técnica que "dibuja" la forma de tus datos reales, sin importar si son simétricos o no.
Es una herramienta estadística que toma tus datos (puntos individuales) y crea una curva continua para mostrar dónde se concentran más.

```py
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid", context="notebook")
tips = sns.load_dataset("tips")

sns.kdeplot(data=tips, x="total_bill")

plt.title("KDE de total_bill (densidad suavizada)")
plt.xlabel("Total de la cuenta (USD)")
plt.ylabel("Densidad")
plt.show()
```

Si quisiera agregar relleno utilizaria `fill = True`


## Relleno de la curva y suavidad
Activá fill=True para rellenar bajo la curva y ajustá bw_adjust para controlar la suavidad (valores mayores generan curvas más suaves).
```py 
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid", context="notebook")
tips = sns.load_dataset("tips")
sns.kdeplot(data=tips, x="total_bill", fill=True, bw_adjust=0.7) # bw_adjust: controla el suavizado de la curva, mientras mayor el valor, más suave
plt.title("KDE con relleno (bw_adjust=0.7)")
plt.show()
```

## Múltiples KDE por categoría
El parámetro hue superpone o separa densidades por grupo, mientras que common_norm=False evita normalizarlas juntas.
```py
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid", context="notebook")
tips = sns.load_dataset("tips")

sns.kdeplot(
    data=tips,
    x="total_bill",
    hue="time",
    fill=True,
    common_norm=False, # densidades independientes
    alpha=0.6
)

plt.title("KDE por Lunch vs Dinner (densidades independientes)")
plt.show()
```


## Combinación de histograma y KDE

Podés superponer un histograma (frecuencias/bins) y una KDE (forma suavizada). Existen dos enfoques principales: superposición en el mismo eje o visualización con doble eje.

### Superposición simple (mismo eje)
Cuando haces ax = sns.histplot(...), Seaborn crea un objeto de tipo Axes, dibuja el histograma en él y te lo devuelve guardado en la variable ax.
Al pasarle ax=ax, le estás diciendo a Seaborn: "No crees un gráfico nuevo; busca el dibujo que ya existe en la variable ax y añade el KDE encima".
```py
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid", context="notebook")
tips = sns.load_dataset("tips")

ax = sns.histplot(
    data=tips, x="total_bill",
    bins=30, stat="density", color="#99c2ff", alpha=0.6, edgecolor=None
)

sns.kdeplot(
    data=tips, x="total_bill",
    color="#003f8c", linewidth=2, ax=ax
)

plt.title("Histograma (densidad) + KDE superpuestos")
plt.xlabel("Total de la cuenta (USD)")
plt.ylabel("Densidad")
plt.show()
```


### Doble eje: barras a la izquierda y KDE a la derecha
Usá doble eje cuando la escala del histograma difiere mucho de la densidad.
```py
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid", context="notebook")
tips = sns.load_dataset("tips")

fig, ax1 = plt.subplots()
# Histograma en eje izquierdo
sns.histplot(
    data=tips, x="total_bill",
    bins=30, color="#a7d8de", alpha=0.7, ax=ax1
)

ax1.set_xlabel("Total de la cuenta (USD)")
ax1.set_ylabel("Frecuencia (histograma)", color="#2c3e50")

# Crear eje derecho para KDE
ax2 = ax1.twinx()
sns.kdeplot(
    data=tips, x="total_bill",
    color="#0b3c49", linewidth=2, ax=ax2
)

ax2.set_ylabel("Densidad (KDE)", color="#0b3c49")

plt.title("Histograma (izq.) + KDE (der.) con ejes separados")
plt.show()