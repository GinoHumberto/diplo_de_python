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



#Escribir un programa en el cual: dada una lista de tres valores numéricos
#distintos se calcule e informe su rango de variación (debe mostrar el mayor y el
#menor de ellos)