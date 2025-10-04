# un error comun en python es tratar dividir por 0, ej:
try:    
    numero = int(input('Numero: '))
    x = 2/numero
except ZeroDivisionError:
    print('el numero no puede ser 0')
numero = int(input('Numero: '))



meses=("enero","febrero","marzo","abril","mayo","junio",
"julio","agosto","septiembre","octubre","noviembre","diciembre")
try:
    nromes=int(input("Ingrese un número de mes [1-12]:"))
    print(meses[nromes-1])
except IndexError:
    print("En número de mes debe ir entre 1 y 12")

meses=("enero","febrero","marzo","abril","mayo","junio",
"julio","agosto","septiembre","octubre","noviembre","diciembre")
try:
    nromes=int(input("Ingrese un número de mes [1-12]:"))
    print(meses[nromes-1])
except:
    print("Problemas con la entrada u operación")