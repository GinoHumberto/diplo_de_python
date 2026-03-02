#import pandas as pd

# # Serie a partir de una lista
# serie = pd.Series([10, 20, 30, 40])
# print("Serie desde lista:")
# print(serie)

# # Serie con índices personalizados
# serie_idx = pd.Series([10, 20, 30, 40], index=["a", "b", "c", "d"])
# print("\nSerie con índices personalizados:")
# print(serie_idx)

# # Serie a partir de un diccionario
# serie_dict = pd.Series({"Ana": 23, "Luis": 35, "Carla": 29})
# print("\nSerie desde diccionario:")
# print(serie_dict)

# # Acceso por índice numérico
# print(serie[0]) # 10

# # Acceso por etiqueta
# print(serie_idx["b"]) # 20

# # Slicing (por posición)
# print(serie[1:3]) # valores 20 y 30

# # Slicing (por etiquetas)
# print(serie_idx["b":"d"])

# # Operaciones aritméticas
# print(serie + 5) # suma 5 a todos los elementos
# print(serie * 2) # multiplica por 2

# # Comparaciones
# print(serie > 25) # devuelve True/False por cada valor

# # Funciones estadísticas
# print("Suma:", serie.sum())
# print("Media:", serie.mean())
# print("Máximo:", serie.max())

# datos2 = [
# {"Nombre": "Ana", "Edad": 23, "Ciudad": "Córdoba"},
# {"Nombre": "Luis", "Edad": 35, "Ciudad": "Buenos Aires"},
# {"Nombre": "Carla", "Edad": 29, "Ciudad": "Rosario"}
# ]
# df2 = pd.DataFrame(datos2)
# print(df2)

# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><> #
#                              Ejemplo SQLite                              #
# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><> #

# import sqlite3
# import pandas as pd

# # Conexión a base SQLite
# conexion = sqlite3.connect("mibase.db")

# # Crear un DataFrame con algunos datos de prueba
# data = {
# "nombre": ["Juan", "María", "Pedro", "Ana"],
# "edad": [25, 30, 35, 28],
# "ciudad": ["Madrid", "Barcelona", "Sevilla", "Valencia"]
# }
# df = pd.DataFrame(data)

# # Guardar un DataFrame en la base de datos
# df.to_sql("personas", conexion, if_exists="replace", index=False)
# print("\nDataFrame guardado en la base de datos 'mibase.db' en la tabla 'personas'.")

# # Leer los datos de la base de datos y guardarlos en otro DataFrame
# df_leido = pd.read_sql("SELECT * FROM personas", conexion)
# print("\nDataFrame leído de la base de datos:")
# print(df_leido)

# # Cerrar la conexión
# conexion.close()
# print("\nConexión a la base de datos cerrada.")



# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><> #
#                          Pandas, Matplot y Numpy                           #
# <><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><> #

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# datos = {
# "Mes": ["Enero", "Febrero", "Marzo", "Abril", "Mayo"],
# "Ventas": [100, 120, 90, 150, 200]
# }
# df = pd.DataFrame(datos)
# # Gráfico de líneas
# df.plot(x="Mes", y="Ventas", kind="line", marker="o", title="Ventas mensuales")
# plt.show()
# df.plot(x="Mes", y="Ventas", kind="bar", title="Ventas por mes")
# plt.show()
# df["Clientes"] = [30, 40, 35, 50, 65]
# df.plot(x="Clientes", y="Ventas", kind="scatter", title="Relación Clientes-Ventas")
# plt.show()


# Histograma de edades

# df_hist = pd.DataFrame({"Edades": np.random.randint(18, 65, size=100)})
# df_hist["Edades"].plot(kind="hist", bins=10, title="Distribución de edades")
# plt.xlabel("Edad")
# plt.show()


# Grafico de caja y bigote 

# df_box = pd.DataFrame({
#     "Ventas_Q1": [100, 120, 130, 110, 140],
#     "Ventas_Q2": [200, 210, 190, 220, 230]
#     })
# df_box.plot(kind="box", title="Distribución de ventas por trimestre")
# plt.show()


# Gráfico de líneas

# fechas = pd.date_range("2024-01-01", periods=6, freq="ME") # aca Freq nos dice que es al fin de mes
# ventas = [100, 120, 115, 150, 180, 200]
# df_line = pd.DataFrame({"Fecha": fechas, "Ventas": ventas})
# df_line.plot(x="Fecha", y="Ventas", kind="line", marker="o", title="Evolución de ventas")
# plt.show()