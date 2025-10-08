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