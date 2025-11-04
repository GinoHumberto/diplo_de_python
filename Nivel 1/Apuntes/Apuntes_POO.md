# Clase 13

Imprtación de modulo, pero nuestro.
Por ej hacemos un módulo con una funcion principal, que luego lo queremos cargar.

En un proyecto priorizar que siempre todo este en un mismo lugar(carpeta o directorio)
Cuando se crean modulos NUNCA poner como nombre nombre de OTROS MODULOS DE PYTHON ya que va a dar un error.

Para importar un modulo, no es tan diferente a lo que haciamos antes, simplemente:
 ```py
import operacioneslista #Nombre del modulo, puede ser cualquiera.

lista = operacioneslista.cargar()
operacioneslista.imprimir_mayor(lista)
operacioneslista.imprimir_suma(lista)
 ```


## Programación orientada a objetos

Es una metodologia de programación.
Clase -> Objeto -> Metodo -> Atributo

Un objeto es una instancia de una clase.
Los objetos son entidades, tienen datos, programación. Es todo aquello que es lit un objeto, un directorio tambien puede ser un objeto.
"Encapsulamiento": ej, un auto tiene motor, ruedas, etc.

Metodos: arrancar, detenerse, etc

En un objeto hay variables y funciones, a eso se refiere el encapsulamiento.


La clase es un *Molde*, del cual luego puedo crear caracteristicas, por ej creamos una clase que se llama "persona"
La clase es un molde que tiene atributos y metodos comunes a todos los objetos de ese tipo.

siguiendo el ej:
```py
class Persona:

    def inicializar(self,nom): # Metodo
        self.nombre=nom
    
    def imprimir(self): # Metodo
        print("Nombre",self.nombre)


# bloque principal
persona1=Persona() # Incorporo a mi variable "persona1" la clase "persona", Persona1 es el objeto
persona1.inicializar("Pedro") # Ingreso el valor del metodo en este caso "Pedro"
persona1.imprimir()
persona2=Persona()
persona2.inicializar("Carla")
persona2.imprimir()
```
*Persona1 es el objeto*

El self es el vinculo con la clase.
Es decir en este caso el self de inicializar, lo que hace es saber que esta dentro de la clase persona, es como buscar una caja de herramientas y queremos un martillo, el self seria la caja.

La clasificación sería: #Clase: Persona, Métodos: inicializar e imprimir, Objeto/variable: persona1, 2, etc...

*Un metodo funciona muy parecido a la funcion, solamente que le pasamos los datos de la clase*

### Metodo ```__init__``` de la clase

Hay un metodo especial de clase que **inicializa atributos para un objeto**
El ```__init__``` cuando creamos el objeto llamo al objeto y se inicializa todo al llamarlo.
"Se llama automáticamente", se ejecuta automaticamente luego de crear un objeto, no puede retornar datos, puede recibir parametros y es opcional.

 ```py
class Empleado:

    def __init__(self):
        self.nombre=input("Ingrese el nombre del empleado: ")
        self.sueldo=float(input("Ingrese el sueldo:"))

    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Sueldo:",self.sueldo)

    def paga_impuestos(self):
        if self.sueldo>3000:
            print("Debe pagar impuestos")
        else:
            print("No paga impuestos")

# bloque principal
empleado1=Empleado()
empleado1.imprimir()
empleado1.paga_impuestos()
  ```

Recordemos que init se llama solo
Cuando creo una clase las funciones dentro de la misma quedan entrelazadas.

# Clase 14
Si queremos llamar al metodo dentro de la clase, Es decir un metodo llama a otro metodo,
```py
self.[nombre_del _metodo]
```
Ej:
```py
class Operacion:
    def __init__ (self):
        self.valor1 = int(input('Numero: '))
        self.valor2 = int(input('Numero: '))
        self.sumar()
        self.resta()
    
    def sumar(self):
        suma = self.valor1 + self.valor2
        print(suma)
    
    def resta(self):
        resta = self.valor1 - self.valor2
        print(resta)
    

operacion1 = Operacion()
```

## POO 2 Colaboración y herencia
Es un sistema donde las clases interactúa y se comunican
### Colaboracion:
Las clases se comunican, es diferente a erencia, ya que no es una clase dentro de otra clase, son dos clases separadas pero que interactuan entre ellas
```py
class Cliente:

    def __init__(self,nombre):
        self.nombre=nombre
        self.monto=0

    def depositar(self,monto):
        self.monto=self.monto+monto

    def extraer(self,monto):
        self.monto=self.monto-monto

    def retornar_monto(self):
        return self.monto

    def imprimir(self):
        print(self.nombre,"tiene depositado la suma de",self.monto)

class Banco:

    def __init__(self):
        self.cliente1=Cliente("Juan")
        self.cliente2=Cliente("Ana")
        self.cliente3=Cliente("Diego")
    
    def operar(self):
        self.cliente1.depositar(100)
        self.cliente2.depositar(150)
        self.cliente3.depositar(200)
        self.cliente3.extraer(150)

    def depositos_totales(self):
        total=self.cliente1.retornar_monto()+self.cliente2.retornar_monto()+self.cliente3.retornar_monto()
        print("El total de dinero del banco es:",total)
        self.cliente1.imprimir()
        self.cliente2.imprimir()
        self.cliente3.imprimir()

# bloque principal
banco1=Banco()
banco1.operar()
banco1.depositos_totales()
```
Podemos ver como la clase Banco, le da a la clase Cliente el nombre del cliente y como la clase banco obtiene lo depositado o extraido de la clase cliente

# Clase 15
Para cortar una línea en varias líneas en Python podemos encerrar entre paréntesis la condición:
```py
if (self.dado1.retornar_valor()==self.dado2.retornar_valor()
and self.dado1.retornar_valor()==self.dado3.retornar_valor()):
```
O agregar una barra al final:
```py
if self.dado1.retornar_valor()==self.dado2.retornar_valor() and \
self.dado1.retornar_valor()==self.dado3.retornar_valor():
```

## Herencia
**Puedo crear nuevas clases partiendo de clases existentes**
Clase padre: Es la que deciende o deriva una clase hija
Clase hija o subclase: Es la clase descendiente de la otra. Hereda los atributos y los metodos de la clase padre.

ejemplos teóricos de herencia:
1) Imaginemos la clase Vehículo. Qué clases podrían derivar de ella?
```
Vehiculo:
    a. Colectivo 
    b. Moto:
        * Suzuki
        * Honda 
    c. Auto:
        * Ford
        * Renault 
```
Siempre hacia abajo en la jerarquía hay una especialización (las subclases añaden nuevos atributos y métodos).

Ej: Plantear una clase Persona que contenga dos atributos: nombre y edad. Definir como responsabilidades la carga por teclado y su impresión. En el bloque principal del programa definir un objeto de la clase persona y llamar a sus métodos.
Declarar una segunda clase llamada Empleado que herede de la clase Persona y agregue un atributo sueldo y muestre si debe pagar impuestos (sueldo superior a 3000) También en el bloque principal del programa crear un objeto de la clase Empleado.

```py
class Persona:
    
    def __init__(self):
        self.nombre=input("Ingrese el nombre:")
        self.edad=int(input("Ingrese la edad:"))
    
    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Edad:",self.edad)

class Empleado(Persona): # Aca vemos que dentro de la clase esta nuestra clase "Persona"
    
    def __init__(self): #Sigue haciendo referencia a la clase empeado, se llama asi mismo
        super().__init__() # ACA ESTA LO IMPORTANTE, tenemos el "super". Este init, llama a un metodo de inicializacion de otra clase, es decir persona
        self.sueldo=float(input("Ingrese el sueldo:"))
    
    def imprimir(self):
        super().imprimir()
        print("Sueldo:",self.sueldo)
    
    def paga_impuestos(self):
        if self.sueldo>3000:
            print("El empleado debe pagar impuestos")
        else:
            print("No paga impuestos")

# bloque principal
persona1=Persona()
persona1.imprimir()
print("____________________________")
empleado1=Empleado() 
empleado1.imprimir()
empleado1.paga_impuestos()
```

Aca estoy creando una clase empleado, pero tiene un parametro que es "Persona", por eso  ```class Empleado(Persona):```
El super es el que indica cuando se hace herencia del parametro de la clase

*~¿Cuando herencia y cuando colaboración?: herencia por ej se usa en robotica, mientras que en colaboración se utiliza en programas con valores que utilizan de otra clase.~*
La herencia seria como un import
La colaboracion seria como un import "xxx" from "xxx" 

## Variables de clase
```py
class Persona:
    
    variable=20
    
    def __init__(self,nombre):
        self.nombre=nombre

# bloque principal
persona1=Persona("Juan")
persona2=Persona("Ana")
persona3=Persona("Luis")

print(persona1.nombre) # Juan
print(persona2.nombre) # Ana
print(persona3.nombre) # Luis
print(persona1.variable) # 20
Persona.variable=5
print(persona2.variable) # 5
print(persona3.variable) # 5 ya que cambio la variable
```

# Clase 16

## Variables de clase
### Variables tipo lista
ej:
```py
class Cliente:
    suspendidos=[]

    def __init__(self,codigo,nombre): # Toma los atributos de cliente
        self.codigo=codigo
        self.nombre=nombre

    def imprimir(self):
        print("Codigo:",self.codigo)
        print("Nombre:",self.nombre)
        self.esta_suspendido()

    def esta_suspendido(self):
        if self.codigo in Cliente.suspendidos:
            print("Esta suspendido")
        else:
            print("No esta suspendido")
        print("_____________________________")

    def suspender(self):
        Cliente.suspendidos.append(self.codigo)

# bloque principal
cliente1=Cliente(1,"Juan")
cliente2=Cliente(2,"Ana")
cliente3=Cliente(3,"Diego")
cliente4=Cliente(4,"Pedro")

cliente3.suspender() # Aca suspendo
cliente4.suspender()

cliente1.imprimir()
cliente2.imprimir()
cliente3.imprimir()
cliente4.imprimir()

print(Cliente.suspendidos)
```

## Herencia
```py
class Operacion:

    def operar(self):
        pass

class xx:
    
    def xx():
        ''
```
Operar va a depender de otras clases. 
El pass esta vacio (es un metodo que sirve para esperar algo)
Operar espera algo, que obtiene lo que espera de otras clases, en el ejemplo completo espera el resultado, el cual proviene del ingreso de otras clases

El pass es el nexo, es el super, de modo que cuando pongo el pass omito colocar el "super" en las otras clases.

Si no coloco ``pass`` o ``super`` la clase xx no va a poder acceder a los datos cargados en operación

## Metodo __str__
Metodo especial que nos permite pasarle un objeto a la funcion y la convierte en string
ej:
```py
class Persona:
d   ef __init__(self,nom,ape):
        self.nombre=nom
        self.apellido=ape

persona1=Persona("Jose","Rodriguez")
print(persona1)

#Nos muestra algo parecido a esto:
#<__main__.Persona object at 0x03E99C90>
```

Si usamos el metodo __str__
```py
class Persona:
    
    def __init__(self,nom,ape):
        self.nombre=nom
        self.apellido=ape
    
    def __str__(self):
        cadena=self.nombre+","+self.apellido
        return cadena

persona1=Persona("Jose","Rodriguez")
print(persona1)
```
EL metodo __str__ se llama solo al igual que __init__

En este caso persona 1 llama automáticamente a la carga del init y a la cadena o conversion del objeto a cadena.
(Suele utilizarse para dar valores para base de datos)

## Redefinición de los operadoes matemáticos con objetos
Para el operador +:
```py
__add__(self,objeto2)
```
Para el operador -:
```py
__sub__(self,objeto2)
```
Para el operador *:
```py
__mul__(self,objeto2)
```
Para el operador //:
```py
__floordiv__(self,objeto2)
```
Para el operador /:
```py
__truediv__(self,objeto2)
```

Ej:
```py
class Cliente:
    
    def __init__(self,nombre,monto):
        self.nombre=nombre
        self.monto=monto
    
    def __add__(self,objeto2):
        s=self.monto+objeto2.monto
        return s

cli1=Cliente('Ana',1200)
cli2=Cliente('Luis',1500)
print("El total depositado por los dos clientes es")
print(cli1+cli2)
```