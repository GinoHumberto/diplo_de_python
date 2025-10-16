# CLASE 1, 9 de septiembre. 
Diplomatura en Python. 

Charla sobre optimización de código y introducción,
dnobile@carreralinux.com.ar Correo del profesor Ubuntudde-imac141
Python clase 1 (abrió ese archivo)
```python
edad (variable) = valor #(donde el valor puede ser determinado o puede ser solicitado, como input)
```
Tipado dinámico significa que las variables no tienen un tipo fijo en tiempo de compilación: 
Puedes asignar distintos tipos a la misma variable en momentos diferentes:
```python
x = 5 (x es int) 
x = "hola" (ahora x es str) 
``` 
No hay una sola forma de realizar un ingreso.
Es fuertemente tipado, ya que si uno opta por definir la variable, por ej `int(input(…))` estamos obligando al programa.

Permiso de ejecución: 
```bash
chmod +x nombre del archivo
```

Se puede asignar mas de 1 variable en la misma linea

Una variable es una expresión cuando: cuando no se sabe algo de el valor previo ej:
```py
valor = argumento_1
```
No se sabe que es `argumento_1`, por lo tanto es una expresión

# Clase 3 16/09
Estructuras de control (If)
Errores sintácticos: son errores tipográficos: `‘, : () {} []` palabras mal escritas como Print en mayúscula.
```py
lado=int(input("Ingrese la medida del lado del cuadrado:"))
superficie=lado*lado
print("La superficie del cuadrado es")
print(Superficie)
# No va a funcionar pq superficie != Superficie 
```

Errores lógicos: Error de mal diagrama de un programa, por ejemplo 
```py
lado=int(input("Ingrese la medida del lado del cuadrado:"))
superficie=lado*lado*lado
print("La superficie del cuadrado es")
print(superficie)
# lado * lado * lado = volumen, no a superficie.
```

Programación secuencial, el programa se ejecuta linea por linea 

# Clase 4 18/09 
Loops while. Ver clases

# Clase 5 23/09
Loops for. Ver clases

# Clase 6 25/09
Se van a ver primero los ejercicios
Funciones: abrio archivo con título "Funciones: parámetros"
Es una reutilizacion de codigo, es un codigo dentro de una abstracción, esto quiere decir que el codigo esta dentro de un bloque, es un programa que esta en un lugar el cual luego llamo.

# Clase 7 30/09
Se abrio funciones en python ejercicios resueltos. ver "funciones.py"
se abrio Funciones teoria y ejercicios
Introduccion de try y except

# Clase 8 2/10 
manejo de excepciones (try / except),
El except puede no estar tipificado en caso de establecer que no importa el error que aparezca lo caputre y muestre una respuesta sin especificar el error especifico o que paso.
El finally es yun bloque que se ejecuta siempre al terminar el programa.

# Clase 9
```py
lista=[[1,2,3], [4,5,6], [7,8,9], [10,11,12]]
# imprimimos la lista completa
print(lista)
print("---------")
# imprimimos la primer componente
print(lista[0])
print("---------")
# imprimimos la primer componente de la lista contenida
# en la primer componente de la lista principal
print(lista[0][0])
print("---------")
# imprimimos con un for la lista contenida en la primer componente
for x in range(len(lista[0])):
    print(lista[0][x])
        print("---------")
# imprimimos cada elemento entero de cada lista contenida en la lista
for k in range(len(lista)):
    for x in range(len(lista[k])):
        print(lista[k][x])
```
Aca hay una lista principal y una lista secundaria la principal es "lista" y la secundaria seria por ejemplo lista [0] = [1,2,3], es decir la lista dentro de la lista

# CREAR EXCEPCIONES

Para crear excepciones tenemos que crear una una clase.

### Por ejemplo queremos crear una excepcion que contenga un punto en el final

```py
class ErrorDeCadena(Exception):
    msg = 'La cadena debe terminar con punto' # esto es lo que nos va a retornar el error

def intro_cadena():
    cadena = input('Ingresa tu cadena que termine con "." ')
    if cadena[-1] != '.':
        raise ErrorDeCadena
    return cadena

try:
    cadena = intro_cadena()
    print(f'bien {cadena}')
except ErrorDeCadena as e:
    print(f'Error: {e.msg}')
```

Hay otra forma de comunicar el error, incluido errores ya dados por python como "ValueError":
```py
class ErrorDeCadena(Exception):
    pass

def intro_cadena():
    cadena = input('Ingresa tu cadena que termine con "." ')
    if cadena[-1] != '.':
        raise ErrorDeCadena('xd')
    elif len(cadena) == 1:
        raise ValueError('Sos wbon')
    return cadena

try:
    cadena = intro_cadena()
    print(f'bien {cadena}')
except ErrorDeCadena as e:
    print(f'Error: {e}')
except ValueError as e:
    print(e)
```

# Clase 10
Como eliminar un elemento de una lista
```py
lista=[10, 20, 30, 40, 50]
print(lista)
lista.pop(0)
lista.pop(1)
lista.pop(2)
print(lista)
```
aca va a eliminar el elemento 0,1,2 es decir va a quedar solo 20 y 40

Esto es porque el elemento q se borra en 0 es el 10, en 1 es el 30 y no el 20 ya que el 20 pasa a ser el elemento 0 cuando se borra el 10.

Ahora si quisieramos borrar, 10, 20, 30 
```py
lista=[10, 20, 30, 40, 50]
print(lista)
for pop in range(3):
    lista.pop(0)
```

tambien se puede borrar un elemento utilizando `del(lista[x])`:
```py
lista=[10, 20, 30, 40, 50]
print(lista)
del(lista[0])
del(lista[1])
del(lista[2])
print(lista) # 20 40
```
## Tuplas

las tuplas llevan parentecis, `tupla = ()`
En cuanto a funcionamiento, los datos de una tupla son inmutables, esot quiere decir que no podemos agregar, modificar o borrar sus elementos

Una lista puede pasar a ser una tupla y visceversa:
```py
fechatupla1=(25, 12, 2016)
print("Imprimimos la primer tupla")
print(fechatupla1)
fechalista=list(fechatupla1)
print("Imprimimos la lista que se le copio la tupla anterior")
print(fechalista)
fechalista[0]=31
print("Imprimimos la lista ya modificada")
print(fechalista)
fechatupla2=tuple(fechalista)
print("Imprimimos la segunda tupla que se le copio la lista")
print(fechatupla2)
```

# Clase 11 

## Listas y tuplas andidadas
Tengo una lista [juan (1, 2)] con una tuola adentro o visceversa. 
Se puede mutar la lista dentro de una tupla, por ej:
```py
alumno=("pedro",[7, 9])
print(alumno)
alumno[1].append(10)
print(alumno)
```
(Ejercicio de paises y su poblacion)

## Diccionarios

Tiene llaves y valores.
```py
productos={"manzanas":39, "peras":32, "lechuga":17}
print(productos)
```
para la clave "peras" tenemos asociado el valor entero 32

## Cadena de caracteres

Ejercicio:Realizar la carga por teclado del nombre, edad y altura de dos personas. Mostrar por pantalla el nombre de la persona con mayor altura.

### Métodos propios de las cadenas de caracteres.

* upper() : devuelve una cadena de caracteres convertida todos sus caracteres a mayúsculas.
* lower() : devuelve una cadena de caracteres convertida todos sus caracteres a minúsculas.
* capitalize() : devuelve una cadena de caracteres convertida a mayúscula solo su primer caracter y todos los demás a minúsculas.

# Clase 12

Tratamiento de archivos de salida
Existen muchos modos de almacenar datos como son los archivos de texto, archivos binarios, bases de datos etc.

Ej:
```py
archi1=open('datos.txt','w') #Archi1 puede llamarse de otra forma, solo es el nombre de la variable. datos es el archivo que estamos abriendo, la 'w' nos deja escrtibir, equivale write
archi1.write('Hola mundo')
archi1.close()
```
si necesitamos que se cree en otra carpeta podemos indicar el path del mismo:
```py
archi1 = open("c:/administracion/datos.txt","w")
```

Para leer se debe remplazar la 'w' por la 'r'
```py
archi1=open("datos.txt","r")
contenido=archi1.read()
print(contenido)
archi1.close()
```

Para leer contenido del archivo de texto linea a linea:
```py
archi1=open("datos.txt","r")
linea=archi1.readline()
while linea!='':
    print(linea, end='')
    linea=archi1.readline()
archi1.close()
# Compactado
archi1=open("datos.txt","r")
for linea in archi1:
print(linea, end='')
archi1.close()
```

Se puede utilizar la 'a' en ves de 'w' o 'r' para agregar lineas o datos sin que borre las lineas actuales o anteriores del archivo

Hay otra forma para abrir un archivo para leer y escribir que es 'r+', dejandonos leer y escribir.

