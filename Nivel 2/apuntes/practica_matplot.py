import matplotlib.pyplot as plt

# ------------------------- #
#       Grafico simple      #
# ------------------------- #

# plt.plot([1, 2, 3, 4], [10, 20, 25, 30])
# plt.title("Ejemplo basico con Matplotlib")
# plt.xlabel("Eje X")
# plt.ylabel("Eje Y")
# plt.show()


# # Podemos hacerlo de otra forma, diciendo explicitamente cual es el eje x y cual el y.

# x = [1, 2, 3, 4, 5]
# y = [2, 4, 6, 8, 10]

# plt.plot(x, y)
# plt.show()


# ------------------------------------- #
#       Grafico con multiples ejes      #
# ------------------------------------- #

# fig, (ax1, ax2) = plt.subplots(1, 2) # 1 fila, 2 columnas

# # Primer grafico
# ax1.plot([1, 2, 3], [1, 4, 9], color="red")
# ax1.set_title("Grafico 1")

# # Segundo grafico
# ax2.plot([1, 2, 3], [1, 2, 3], color="blue")
# ax2.set_title("Grafico 2")
# plt.show()



# fig, axs = plt.subplots(2, 2) # 2 filas, 2 columnas

# axs[0, 0].plot([1, 2, 3], [1, 2, 3])
# axs[0, 0].set_title("Arriba Izq.")

# axs[0, 1].plot([1, 2, 3], [1, 4, 9])
# axs[0, 1].set_title("Arriba Der.")

# axs[1, 0].plot([1, 2, 3], [1, 8, 27])
# axs[1, 0].set_title("Abajo Izq.")

# axs[1, 1].plot([1, 2, 3], [1, 16, 81])
# axs[1, 1].set_title("Abajo Der.")

# plt.tight_layout() # Ajusta espacios, es el que hace que no se superpongan.
# plt.show()

# ----------------- #
#       Colores     #
# ----------------- #

# x = [1, 2, 3, 4, 5]
# y1 = [2, 4, 6, 8, 10]
# y2 = [1, 3, 5, 7, 9]

# plt.plot(x, y1, color="blue", label="Linea Azul")
# plt.plot(x, y2, color="#FF5733", label="Linea Naranja")
# plt.legend()
# plt.show()

# ----------------- #
#       Limites     #
# ----------------- #

# x = [0, 1, 2, 3, 4, 5, 6]
# y = [0, 1, 4, 9, 16, 25, 36]

# plt.plot(x, y, marker="o")
# plt.title("Ejemplo con limites de ejes")
# plt.xlim(0, 6) # Limite para el eje X
# plt.ylim(0, 40) # Limite para el eje Y
# plt.show()

# ----------------- #
#       Leyenda     #
# ----------------- #

# x = [1, 2, 3, 4]
# y1 = [1, 4, 9, 16]
# y2 = [1, 2, 3, 4]

# plt.plot(x, y1, label="Cuadrados")
# plt.plot(x, y2, label="Lineal")
# plt.legend(loc="upper left")
# plt.title("Leyenda en la esquina superior izquierda")
# plt.show()

# -------------------------- #
#       Etiqueta en ejes     #
# -------------------------- #

# x = [1, 2, 3, 4]
# y = [1, 4, 9, 16]
# plt.plot(x, y)
# plt.xlabel("Valores de X")
# plt.ylabel("Valores de Y")
# plt.title("Ejemplo con etiquetas en los ejes")
# plt.show()

# --------------------- #
#       Anotaciones     #
# --------------------- #

# x = [1, 2, 3, 4, 5]
# y = [1, 4, 9, 16, 25]

# plt.plot(x, y, marker="o")
# plt.title("Anotacion de un punto clave")
# plt.annotate(
#     "Aqui esta 3",
#     xy=(3, 9),
#     xytext=(4, 12),
#     arrowprops=dict(facecolor="black", shrink=0.05, width = 1) 
# )
# plt.show()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

# ~~~ GRAFICOS AVANZADOS ~~~ #

# -------------------------- #
#       Grafico de torta     #
# -------------------------- #

# fig, ax = plt.subplots()

# valores = [40, 25, 20, 15]
# labels = ["Ventas", "Marketing", "I+D", "Operaciones"]
# explode = [0.05, 0, 0, 0] # Resaltar "Ventas"

# ax.pie(
#     valores,
#     labels=labels,
#     explode=explode,
#     autopct="%.1f%%",
#     startangle=90,
#     wedgeprops={"linewidth": 1, "edgecolor": "white"}
# )

# ax.set_title("Distribución de presupuesto")
# ax.set_aspect('equal') # Círculo perfecto
# plt.show()

# -------------------------- #
#       Grafico de área      #
# -------------------------- #

# import numpy as np

# x = np.linspace(0, 2 * np.pi, 300)
# y1 = np.sin(x) + 1
# y2 = np.cos(x) + 1

# fig, ax = plt.subplots()
# ax.plot(x, y1, label="Seno")
# ax.plot(x, y2, label="Coseno", color = "blue")
# ax.fill_between(x, y1, y2, where=(y1 >= y2), alpha=0.25, label="Área (y1 >= y2)")
# ax.fill_between(x, y1, y2, where=(y1 < y2), alpha=0.25, label="Área (y1 < y2)")

# ax.set_title("Área entre dos curvas")
# ax.set_xlabel("Ángulo")
# ax.set_ylabel("Valor")
# ax.legend()
# plt.show()

# ------------------------------ #
#       Grafico de densidad      #
# ------------------------------ #

# import numpy as np

# np.random.seed(42)
# muestras = np.random.normal(loc=0, scale=1, size=2000)
# fig, ax = plt.subplots()

# # Histograma como densidad
# ax.hist(
#     muestras,
#     bins="auto",
#     density=True,
#     edgecolor="black",
#     alpha=0.4,
#     label="Hist (densidad)"
# )

# # Curva normal estimada con media y desvío de los datos
# mu, sigma = np.mean(muestras), np.std(muestras, ddof=1)
# x = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 400)
# pdf = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)
# ax.plot(x, pdf, linewidth=2, label=f"N(mu={mu:.2f}, sigma={sigma:.2f})")

# ax.set_title("Distribución y densidad (hist con density=True)")
# ax.set_xlabel("Valor")
# ax.set_ylabel("Densidad")
# ax.legend()
# plt.show()

# ----------------------------- #
#       Diagrama de error       #
# ----------------------------- #

# import numpy as np

# x = np.arange(1, 6)
# y = np.array([2.0, 2.5, 3.7, 3.2, 4.1])
# yerr = np.array([0.2, 0.3, 0.25, 0.35, 0.2]) # Error vertical

# fig, ax = plt.subplots()

# ax.errorbar(
#     x,
#     y,
#     yerr=yerr,
#     fmt="o-", # Marcador + línea
#     capsize=4, # Tapa de las barras de error
#     elinewidth=1.2, # Grosor de la barra de error
#     label="Medición con error"
# )

# ax.set_title("Diagrama de error (errorbar)")
# ax.set_xlabel("Muestra")
# ax.set_ylabel("Valor medido")
# ax.legend()
# plt.show()

# --------------------------------------- #
#       Subplots, figuras multiples       #
# --------------------------------------- #

# import numpy as np

# x = np.linspace(0, 2 * np.pi, 200)

# # Sintaxis moderna: Figure y arreglo de Axes
# fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(8, 6), layout='constrained')
# # 'layout="constrained"' ayuda a evitar solapamientos de textos y etiquetas.


# # Función 1
# axs[0, 0].plot(x, np.sin(x)) # con axs[m,n] determinamos la posicion del gráfico, con lo que sigue, determinamos el grafico en sí
# axs[0, 0].set_title("sin(x)")

# # Función 2
# axs[0, 1].plot(x, np.cos(x), linestyle="--")
# axs[0, 1].set_title("cos(x)")

# # Función 3
# axs[1, 0].plot(x, np.tan(x))
# axs[1, 0].set_title("tan(x)")
# axs[1, 0].set_ylim(-3, 3) # Acotar tan(x)

# # Función 4
# axs[1, 1].plot(x, np.sin(x) * np.cos(x), marker="o", markersize=2, linestyle="-")
# axs[1, 1].set_title("sin(x)*cos(x)")

# fig.suptitle("Cuadrícula 2x2 con subplots", fontsize=12)
# plt.show()

# ------------------------------------------------ #
#       Subplots, figuras que comparten ejes       #
# ------------------------------------------------ #
# import numpy as np

# t = np.linspace(0, 10, 500)
# s1 = np.sin(t)
# s2 = np.cos(t)

# fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(8, 5), layout='constrained') # aquí colocamos sharex

# ax1.plot(t, s1, label="sin(t)")
# ax1.set_ylabel("Amplitud")
# ax1.legend()

# ax2.plot(t, s2, color="orange", label="cos(t)")
# ax2.set_xlabel("Tiempo")
# ax2.set_ylabel("Amplitud")
# ax2.legend()

# fig.suptitle("Subplots compartiendo eje X")
# plt.show()

# -------------------------------- #
#       Diseños con Gridspec       #
# -------------------------------- #
import numpy as np
from matplotlib.gridspec import GridSpec

x = np.linspace(0, 2 * np.pi, 300)

fig = plt.figure(figsize=(9, 6), layout='constrained')

gs = GridSpec(nrows=2, ncols=2, figure=fig, height_ratios=[2, 1])

ax_top = fig.add_subplot(gs[0, :])
ax_top.plot(x, np.sin(x), label="sin(x)")
ax_top.plot(x, np.cos(x), label="cos(x)")
ax_top.set_title("Superior: sin y cos")
ax_top.legend()

ax_bl = fig.add_subplot(gs[1, 0])
ax_bl.plot(x, np.sin(2 * x), color="purple")
ax_bl.set_title("Inferior Izq: sin(2x)")

ax_br = fig.add_subplot(gs[1, 1])
ax_br.plot(x, np.cos(2 * x), color="green")
ax_br.set_title("Inferior Der: cos(2x)")

fig.suptitle("Diseño avanzado con GridSpec (1 grande arriba, 2 abajo)")
plt.show()

# -------------------------- #
#       Estilos y temas      #
# -------------------------- #

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

# ------------------------- #
#       Dispersion 3d       #
# ------------------------- #

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