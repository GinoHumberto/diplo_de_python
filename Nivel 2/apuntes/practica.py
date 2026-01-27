import pandas as pd

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

datos2 = [
{"Nombre": "Ana", "Edad": 23, "Ciudad": "Córdoba"},
{"Nombre": "Luis", "Edad": 35, "Ciudad": "Buenos Aires"},
{"Nombre": "Carla", "Edad": 29, "Ciudad": "Rosario"}
]
df2 = pd.DataFrame(datos2)
print(df2)