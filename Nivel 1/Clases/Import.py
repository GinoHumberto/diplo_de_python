import random

# dado1=random.randint(1,6)
# dado2=random.randint(1,6)
# print("Primer dado:",dado1)
# print("Segundo dado:",dado2)
# suma=dado1+dado2
# if suma==7:
#     print("Gano")
# else:
#     print("Perdio")
"""
def cargar():
    lista=[]
    for x in range(10):
        lista.append(random.randint(0,1000))
    return lista

def imprimir(lista):
    print(lista)

def mezclar(lista):
    random.shuffle(lista)

lista=cargar()
print("Lista generada aleatoriamente")

imprimir(lista)

mezclar(lista)
print("La misma lista luego de mezclar")

imprimir(lista)
"""
#####################
#       Math        #
#####################

from math import sqrt, pow
valor=int(input("Ingrese un valor entero:"))
r1=sqrt(valor)
r2=pow(valor,3)
print("La raiz cuadrada es",r1)
print("El cubo es",r2)