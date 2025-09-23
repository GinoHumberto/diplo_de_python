# March/case sirve para conparar o entrar No hay diferencias, es como un switch, es simplemente otra forma de hacerlo.
# La unica diferencia es que if ejecuta condiciones basados en booleanos y match se usa para la coincidencia de patrones.
'''
dia = 'Lunes'
match dia:
    case 'viernes':
        print('ultimo dia laboral')
    case 'Lunes':
        print('buen comienzo')
    case _:
        print('otro dia')

#Ejemplo de puntaje

puntaje = 85
match puntaje:
    case 100:
        ('Perfecto')
    case 90|80|70:
        print('Buen trabajo')
    case _ if puntaje < 60:
        print('reprobado')
    case _:
        print('Puntaje válido pero no destacado')

# estructuras repetitivas
# Ejecuta una instruccion o muchas instructuras varias veces

#x=1
#while x<=100:
#    print(x)
#    x=x+1 (Iterador)

x=1 # Contador, va a detener el programa cuando se cumpla 
suma=0 #acumulador (acumula los cambios que realiza la x)
while x<=10:
    valor=int(input("Ingrese un valor:"))
    suma=suma+valor
    x=x+1
promedio=suma/10
print("La suma de los 10 valores es")
print(suma)
print("El promedio es")
print(promedio)

#For quedo pendiente

for x in range(100):
    print(x)

for x in range(1,100, 2): #empieza en 1 y va en 2, es decir 1, 3, 5, 7...
    print(x)

for x in range(100,2, -1): #empieza en 100 y va restando 1 hasta llegar al 3.
    print(x)

suma=0
for f in range(10):
    valor=int(input("Ingrese valor:"))
    suma=suma+valor
print("La suma es")
print(suma)
promedio=suma/10
print("El promedio es:")
print(promedio)
'''

#codificar un programa que lea n números enteros y calcule la cantidad de valores mayores o iguales a 1000(n se carga por teclado).
#Este tipo de problemas también se puede resolver empleando la estructura repetitiva for. Lo primero que se hace es cargar una variable que indique la cantidad de valores a ingresar. Dicha variable se carga antes de entrar a la estructura repetitiva for.

n = int(input('Ingeresa la cantidad de veces que se van a leer numeros enteros: '))

mayores = 0 
menores = 0
for valor in range(n):
    valor = int(input('ingresa tu valor: '))
    if valor >= 1000:
        mayores += 1
    else:
        menores += 1
print(f'La cantidad de valores mayores de 1000 son {mayores}, los valores menores de 1000 son {menores}')

