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