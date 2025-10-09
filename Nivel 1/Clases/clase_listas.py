# nombres=[]
# notas=[]

# for x in range(3):
#     nom=input("Ingrese el nombre del alumno:")
#     nombres.append(nom)
#     no1=int(input("Ingrese la primer nota:"))
#     no2=int(input("Ingrese la segunda nota:"))
#     notas.append([no1,no2])

# for x in range(3):
#     print(nombres[x],notas[x][0],notas[x][1])

# como vemos la longitud de una lista dentro de una lista

lista=[10, 20, 30, 40, 50]
print(lista)
lista.pop(0)
lista.pop(1)
lista.pop(2)
print(lista)

lista=[10, 20, 30, 40, 50]
print(lista)
for pop in range(3):
    lista.pop(0)
print(lista)