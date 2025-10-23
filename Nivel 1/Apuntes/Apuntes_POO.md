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
