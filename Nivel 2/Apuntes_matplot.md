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

