# Primer ejercicio
def cantidad_vocales(cadena): #La funcion con su nombre y su parametro
    cant=0
    for x in range(len(cadena)): # Se utiliza el for para ir por cada letra de la palabra, el range(len(cadena)) es para que itere y vaya por cada letra del total de letras de la palabra
        if cadena[x]=="a" or cadena[x]=="e" or cadena[x]=="i" or cadena[x]=="o" or cadena[x]=="u": # Aca "x" es la letra de la palabra por eso esta dentro del corchete, ya que va a ser el numero de la letra ej[0](es la h en caso de hola), y luego ve si dicha letra es igual a una vocal.
            cant=cant+1
    print("Cantidad de vocales de la palabra",cadena,"es",cant)

cantidad_vocales("hola")
cantidad_vocales("administracion")
cantidad_vocales("correr")

#este programa no cuenta en si vocales, cuenta una posiciones. 

#Confeccionar una función que le enviemos como parámetro el valor del lado de un cuadrado y nos retorne su superficie.

def retornar_superficie(lado):
    sup=lado*lado
    return sup

va=int(input("Ingrese el valor del lado del cuafrado:"))
superficie=retornar_superficie(va)
print("La superficie del cuadrado es",superficie)

# Plantear una función que reciba un string en mayúsculas o minúsculas y retorne la cantidad de letras 'a' o 'A'.
def cantidad_vocal_a(palabra):
    cant=0
    for x in range(len(palabra)):
        if palabra[x]=='a' or palabra[x]=="A":
            cant=cant+1
    return cant
palabra=input("Ingrese una palabra:")
print("La palabra",palabra,"tiene",cantidad_vocal_a(palabra),"a")

#A una funcion se le puede dar un valor por defecto, por ej: (a, b=0, c=0), en este caso el parametro b y c en caso de que no se coloque nada van a valer 0, en el caso de que coloque un parametro, esto se va a cambiar. Ej:
def titulo_subrayado(titulo,caracter="*"): #El asterisco es un valor por defecto del parametro, en los casos de la linea 41 a 43, se lo remplaza por otro valor.
    print(titulo)
    print(caracter*len(titulo))
# bloque principal
titulo_subrayado("Sistema de Administracion")
titulo_subrayado("Ventas","-")
titulo_subrayado('compras', 5) #aca multiplica 5 por la cantidad de letras de la palabra "compras"
titulo_subrayado('compras', '5') #aca multiplica la str 5 por la cantidad de letras de la palabra compras, por lo tanto va a ser 7 veces 5.