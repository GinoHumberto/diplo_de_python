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

fig, (ax1, ax2) = plt.subplots(1, 2) # 1 fila, 2 columnas

# Primer grafico
ax1.plot([1, 2, 3], [1, 4, 9], color="red")
ax1.set_title("Grafico 1")

# Segundo grafico
ax2.plot([1, 2, 3], [1, 2, 3], color="blue")
ax2.set_title("Grafico 2")
plt.show()



fig, axs = plt.subplots(2, 2) # 2 filas, 2 columnas

axs[0, 0].plot([1, 2, 3], [1, 2, 3])
axs[0, 0].set_title("Arriba Izq.")

axs[0, 1].plot([1, 2, 3], [1, 4, 9])
axs[0, 1].set_title("Arriba Der.")

axs[1, 0].plot([1, 2, 3], [1, 8, 27])
axs[1, 0].set_title("Abajo Izq.")

axs[1, 1].plot([1, 2, 3], [1, 16, 81])
axs[1, 1].set_title("Abajo Der.")

plt.tight_layout() # Ajusta espacios, es el que hace que no se superpongan.
plt.show()