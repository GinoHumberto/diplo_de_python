# Realizar un programa que solicite la carga por teclado de dos números, si el
# primero es mayor al segundo informar su suma y diferencia, en caso contrario
# informar el producto y la división del primero respecto al segundo.

'''
print('Si el valor 1 es mas grande que el valor 2 se sumaran y se dara la diferencia, sino se informara el producto y división')
valor_1 = int(input('Ingresa el primer valor: '))
valor_2 = int(input('Ingresa el segundo valor: '))

if valor_1 > valor_2:
    print(f'la suma de tus valores es {valor_1 + valor_2} la diferencia es {valor_1 - valor_2}')
else:
    print(f'El producto de tus valores es {valor_1 * valor_2}, la division{valor_1 / valor_2}')
'''

# Se ingresan tres notas de un alumno, si el promedio es mayor o igual a siete
# mostrar un mensaje "Promocionado"

'''
q_notas = 0
sum_num = 0
while q_notas != 3:
    num = int(input('Ingresa la nota de tu alumno: '))
    nota = num + sum_num
    sum_num = nota
    q_notas += 1
promedio = sum_num/q_notas
if promedio >= 7:
    print('Promocionado')
'''

# Se ingresa por teclado un número positivo de uno o dos dígitos (1..99) mostrar
# un mensaje indicando si el número tiene uno o dos dígitos.
# (Tener en cuenta que condición debe cumplirse para tener dos dígitos un
# número entero)

'''
numero = int(input('Ingresa tu numero de 1 o 2 digitos: '))
while numero > 99:
    numero = int(input('Ingresa tu numero de 1 o 2 digitos: '))

if numero < 10:
    print('Tu número tiene un dígito')
else:
    print('Tu número tiene 2 dígitos')
'''

# Se cargan por teclado tres números distintos. Mostrar por pantalla el mayor
# de ellos.

'''
num_1 = int(input('Ingresa tu primer valor: '))
num_2 = int(input('Ingresa tu segundo valor: '))
num_3 = int(input('Ingresa tu tercer valor: '))

if num_1 > num_2 and num_1 > num_3:
    print(f'tu primer valor es el mayor que es {num_1}')
elif num_2 > num_1 and num_2 > num_3:
    print(f'tu segundo valor es el mayor que es {num_2}')
else:
    print(f'tu tercer valor es el mayor que es {num_3}')
'''
'''
cantidad_num = 0
numero = 0
while 3 != cantidad_num:
    valor = int(input('Ingresa tu valor: '))
    if valor > numero:
        numero = valor
    cantidad_num += 1
print(f'El número mayor es {numero}')
'''

# Se ingresa por teclado un valor entero, mostrar una leyenda que indique si el
# número es positivo, negativo o nulo (es decir cero)

'''
ingreso = int(input('Ingresa tu valor: '))
if ingreso > 0:
    print('tu número es positivo')
elif ingreso == 0:
    print('tu número es 0')
else:
    print('tu número es negativo')
'''

# Confeccionar un programa que permita cargar un número entero positivo de
# hasta tres cifras y muestre un mensaje indicando si tiene 1, 2, o 3 cifras.
# Mostrar un mensaje de error si el número de cifras es mayor.

'''
numero = int(input('Ingresa tu numero de 1 o 3 digitos: '))
while numero > 999:
    numero = int(input('Ingresa tu numero de 1 o 3 digitos: '))

if numero < 10:
    print('Tu número tiene un dígito')
elif numero > 10 and numero <100:
    print('Tu número tiene 2 dígitos')
else:
    print('Tu número tiene 3 dígitos')
'''

# Un postulante a un empleo, realiza un test de capacitación, se obtuvo la
# siguiente información: cantidad total de preguntas que se le realizaron y la
# cantidad de preguntas que contestó correctamente. Se pide confeccionar un
# programa que ingrese los dos datos por teclado e informe el nivel del mismo
# según el porcentaje de respuestas correctas que ha obtenido, y sabiendo que:
# Nivel máximo: Porcentaje>=90%.
# Nivel medio: Porcentaje>=75% y <90%.
# Nivel regular: Porcentaje>=50% y <75%.
# Fuera de nivel: Porcentaje<50%.

'''
cantidad_preguntas = int(input('Cuantas preguntas se le hicieron: '))
cantidad_respuestas = int(input('Cuantas preguntas se respondieron bien: '))

promedio = cantidad_respuestas/cantidad_preguntas
if promedio >= 0.9:
    print('Nivel máximo')
elif promedio < 0.9 and promedio >= 0.75:
    print('Nivel medio')
elif promedio < 0.75 and promedio >= 0.5:
    print('Nivel regular')
else:
    print('Fuera de nivel')
'''

#Realizar un programa que pida cargar una fecha cualquiera, luego verificar si
#dicha fecha corresponde a Navidad.

'''
dia = int(input('Ingresa el dia: '))
mes = int(input('Ingresa el mes: '))
if dia == 25 and mes == 12:
    print('Es Navidad')
'''

#Se ingresan por teclado tres números, si todos los valores ingresados son
#menores a 10, imprimir en pantalla la leyenda "Todos los números son
#menores a diez".

'''
val_1 = int(input('Ingresa el primer valor: '))
val_2 = int(input('Ingresa el segundo valor: '))
val_3 = int(input('Ingresa el tercer valor: '))
if val_1 < 10 and val_2 < 10 and val_3 < 10:
    print('Todos tus valores son menor que 10')
'''

#Se ingresan por teclado tres números, si al menos uno de los valores
#ingresados es menor a 10, imprimir en pantalla la leyenda "Alguno de los
#números es menor a diez".

'''
val_1 = int(input('Ingresa el primer valor: '))
val_2 = int(input('Ingresa el segundo valor: '))
val_3 = int(input('Ingresa el tercer valor: '))
if val_1 < 10 or val_2 < 10 or val_3 < 10:
    print('Alguno o todos tus valores son menor que 10')
'''

#Se ingresan tres valores por teclado, si todos son iguales se imprime la suma
#del primero con el segundo y a este resultado se lo multiplica por el tercero.
'''
val_1 = int(input('Ingresa el primer valor: '))
val_2 = int(input('Ingresa el segundo valor: '))
val_3 = int(input('Ingresa el tercer valor: '))
if val_1 == val_2 and val_2 == val_3:
    suma = val_1 + val_2
    print(f'La suma del valor 1 con el valor 2 es {suma} y su multiplicacion por el valor 3 es {suma * val_3}')
'''
#Escribir un programa que pida ingresar la coordenada de un punto en el
#plano, es decir dos valores enteros x e y (distintos a cero).
#Posteriormente imprimir en pantalla en que cuadrante se ubica dicho punto.
#(1º Cuadrante si x > 0 Y y > 0 , 2º Cuadrante: x < 0 Y y > 0, etc.)
'''
x_value = float(input('inserta tu valor del eje x: '))
y_value = float(input('inserta tu valor del eje y: '))

if x_value < 0 and y_value < 0:
    print('tu valor se encuentra en el 3er cuadrante')
elif x_value > 0 and y_value > 0:
    print('tu valor se encuentra en el 1er cuadrante')
elif x_value < 0 and y_value > 0:
    print('tu valor se encuentra en el 2do cuadrante')
elif x_value > 0 and y_value < 0:
    print('tu valor se encuentra en el 4to cuadrante')
elif x_value == 0 and y_value == 0:
    print('tu valor se encuentra en el origen de coordenadas')
elif x_value == 0:
    print('tu valor se encuentra en la rama del eje x')
else:
     print('tu valor se encuentra en la rama del eje y')
'''

#De un operario se conoce su sueldo y los años de antigüedad. Se pide
#confeccionar un programa que lea los datos de entrada e informe:
#a) Si el sueldo es inferior a 500 y su antigüedad es igual o superior a 10 años,
#otorgarle un aumento del 20 %, mostrar el sueldo a pagar.
#b)Si el sueldo es inferior a 500 pero su antigüedad es menor a 10 años,
#otorgarle un aumento de 5 %.
#c) Si el sueldo es mayor o igual a 500 mostrar el sueldo en pantalla sin
#cambios.
'''
salary = int(input('Ingresa el sueldo del operario: '))
antigüedad = int(input('Ingresa los años que lleva trabajando en la empresa: '))

if salary < 500 and antigüedad > 10:
    print(f'El sueldo a pagar es {salary*0.20+salary}')
elif salary < 500 and antigüedad < 10:
    print(f'El sueldo a pagar es {salary*0.05+salary}')
else:
    print(salary)
'''
#Escribir un programa en el cual: dada una lista de tres valores numéricos
#distintos se calcule e informe su rango de variación (debe mostrar el mayor y el
#menor de ellos)

#considerando la variacion como la diferencia:
'''
def dif (num1, num2):
    dif = num1 - num2
    if dif < 0:
        dif = dif*-1
    return(dif)

valores = []
while len(valores) < 3:
    valor = int(input('Ingresa tu valor: '))
    valores.append(valor)
print('Tus valores son', valores)

dif1 = dif(valores[1], valores[2])
dif2 = dif(valores[0], valores[1])
dif3 = dif(valores[0], valores[2])
print(dif1, dif2, dif3)

#mayor:
if dif1 > dif2 and dif1 > dif3:
    print(f'la mayor diferencia es {dif1} que es la diferencia ente {valores[1], valores[2]}')
elif dif2 > dif1 and dif2 > dif3:
    print(f'la mayor diferencia es {dif2} que es la diferencia ente {valores[0], valores[1]}')
else:
    print(f'la mayor diferencia es {dif3} que es la diferencia ente {valores[0], valores[2]}')
#menor:
if dif1 < dif2 and dif1 < dif3:
    print(f'la menor diferencia es {dif1} que es la diferencia ente {valores[1], valores[2]}')
elif dif2 < dif1 and dif2 < dif3:
    print(f'la menor diferencia es {dif2} que es la diferencia ente {valores[0], valores[1]}')
else:
    print(f'la menor diferencia es {dif3} que es la diferencia ente {valores[0], valores[2]}')
'''
#Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe
#cuántos tienen notas mayores o iguales a 7 y cuántos menores.
'''
mayor7 = 0
menor7 = 0
operaciones = 0 
while operaciones < 10:
    solicitud = int(input('Ingresa la nota: '))
    while solicitud < 0 or solicitud > 10:
        solicitud = int(input('Debe ser mayor que 0 y menor a 10: '))
    if solicitud >= 7:
        mayor7 += 1
    else:
        menor7 += 1
    operaciones += 1
print(f'Hay {mayor7} alumnos con notas mayores a 7 y {menor7} con notas menores a 7')
'''
#Se ingresan un conjunto de n alturas de personas por teclado. Mostrar la
#altura promedio de las personas.
'''
alturas = []
n = int(input('Ingresa cuanta gente va a ser parte del estudio: '))
while n < 0:
    n = int(input('Ingresa cuanta gente va a ser parte del estudio: '))
while len(alturas) != n:
    altura = int(input('Ingresa la altura: '))
    alturas.append(altura)
print(f'El promedio de alturas es {sum(alturas)/n}')
'''
#En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y
#$500, realizar un programa que lea los sueldos que cobra cada empleado e
#informe cuántos empleados cobran entre $100 y $300 y cuántos cobran más
#de $300. Además el programa deberá informar el importe que gasta la
#empresa en sueldos al personal.
'''
#Toma de datos
n = int(input('Ingresa cuanta gente va a ser parte del estudio: '))
while n < 0:
    n = int(input('Ingresa cuanta gente va a ser parte del estudio: '))
#calculo de sueldos
operaciones = 0
sueldos_altos = 0
sueldos_bajos = 0
gasto_total = 0
while operaciones != n:
    sueldo = int(input('Ingresa el sueldo del empleado: '))
    while sueldo < 100 or sueldo > 500:
        sueldo = int(input('El sueldo no puede ser un valor atipico, ingresa un sueldo verdadero: '))
    if sueldo > 300:
        sueldos_altos += 1
    else:
        sueldos_bajos += 1
    gasto_total += sueldo
    operaciones += 1
print(f'Hay {sueldos_altos} personas con sueldo alto, hay {sueldos_bajos} personas con sueldo bajo y la empresa gasta: {gasto_total}')
'''
#Realizar un programa que imprima 25 términos de la serie 11 - 22 - 33 - 44,
#etc. (No se ingresan valores por teclado)
'''
n = 25
times = 0
number = 0
while n != times:
    if number < 99:
        number += 11
    elif number > 100 and number < 999 :
        number += 111
    elif number == 999:
        number += 112
    elif number > 999:
        number += 1111
    else:
        number += 12
    times += 1
    print(number)
'''
#Mostrar los múltiplos de 8 hasta el valor 500. Debe aparecer en pantalla 8 - 16
#- 24, etc.
'''
calculo = 0
multiplo = 1
while calculo < 500:
    calculo = multiplo * 8
    multiplo += 1
    if calculo < 500:
        print(calculo)
'''
#Realizar un programa que permita cargar dos listas de 15 valores cada una.
#Informar con un mensaje cual de las dos listas tiene un valor acumulado
#mayor (mensajes "Lista 1 mayor", "Lista 2 mayor", "Listas iguales")
#Tener en cuenta que puede haber dos o más estructuras repetitivas en un
#algoritmo.
'''
def entrada(rango):
    n = 0
    lista = []
    while n < rango:
        valor = int(input('Ingresa tus valores '))
        while valor < 0:
            valor = int(input('Debe ser positivo '))
        lista.append(valor)
        n += 1
    return(lista)

print('Primera lista')
lista1 = entrada(15)
print(lista1)
print('Segunda lista')
lista2 = entrada(15)
print(lista2)

if sum(lista1) > sum(lista2):
    print('La lista 1 es mayor')
elif sum(lista1) == sum(lista2):
    print('Ambas listas son iguales')
else:
    print('La lista 2 es mayot')
'''
#Desarrollar un programa que permita cargar n números enteros y luego nos
#informe cuántos valores fueron pares y cuántos impares.
#Emplear el operador “%” en la condición de la estructura condicional (este
#operador retorna el resto de la división de dos valores, por ejemplo 11%2
#retorna un 1):
#if valor%2==0:
'''
q_valores = int(input('Ingresa cuantos numeros enteros vas a cargar '))
while q_valores < 0:
    q_valores = int(input('El número debe ser positivo '))

impares = 0
pares = 0
n = 0

while n != q_valores:
    valor = int(input('Ingresa tu valor '))
    if valor %2 == 0:
        pares += 1
    else:
        impares += 1
    n += 1
print(f'ingresaste {impares} valor(es) impares y {pares} pares')
'''
# Confeccionar un programa que lea n pares de datos, cada par de datos
# corresponde a la medida de la base y la altura de un triángulo. El programa
# deberá informar:
# a) De cada triángulo la medida de su base, su altura y su superficie.
# b) La cantidad de triángulos cuya superficie es mayor a 12.



# Desarrollar un programa que solicite la carga de 10 números e imprima la
# suma de los últimos 5 valores ingresados.



# Desarrollar un programa que muestre la tabla de multiplicar del 5 (del 5 al 50)



# Confeccionar un programa que permita ingresar un valor del 1 al 10 y nos
# muestre la tabla de multiplicar del mismo (los primeros 12 términos)
# Ejemplo: Si ingreso 3 deberá aparecer en pantalla los valores 3, 6, 9, hasta el
# 36.



# Realizar un programa que lea los lados de n triángulos, e informar:
# a) De cada uno de ellos, qué tipo de triángulo es: equilátero (tres lados
# iguales), isósceles (dos lados iguales), o escaleno (ningún lado igual)
# b) Cantidad de triángulos de cada tipo.



# Escribir un programa que pida ingresar coordenadas (x,y) que representan
# puntos en el plano.
# Informar cuántos puntos se han ingresado en el primer, segundo, tercer y
# cuarto cuadrante. Al comenzar el programa se pide que se ingrese la cantidad
# de puntos a procesar.



# Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
# a) La cantidad de valores ingresados negativos.
# b) La cantidad de valores ingresados positivos.
# c) La cantidad de múltiplos de 15.
# d) El valor acumulado de los números ingresados que son pares.



# Se cuenta con la siguiente información:
# Las edades de 5 estudiantes del turno mañana
# Las edades de 6 estudiantes del turno tarde.
# Las edades de 11 estudiantes del turno noche.
# Las edades de cada estudiante deben ingresarse por teclado.
# a) Obtener el promedio de las edades de cada turno (tres promedios)
# b) Imprimir dichos promedios (promedio de cada turno)
# c) Mostrar por pantalla un mensaje que indique cual de los tres turnos tiene un
# promedio de edades mayor.
