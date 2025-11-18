from empresa import Empresa, NoHayColectivoLibreError
from colectivo import DestinoYaAsignadoError

def menu():
    print(
        '1. Asignar destino a colectivo\n'
        '2. Dar boleto\n'
        '3. Finalizar'
    )

def definir_destino():
    destinos = {}
    n = int(input('Cuantos destinos tiene la empresa: '))
    for i in range(n):
        destinos[i] = input(f'Ingresa el destino {i}: ')
    return destinos

def seleccionar_destino(destinos):
    print(destinos)
    indice = int(input('Ingresa segun el numero a donde quieres que vaya: '))
    return destinos.get(indice)

#Asignar datos principales
nombre = input('Ingresa el nombre de la empresa; ')
cantidad_colectivos = int(input('Cuantos colectivos tiene la empresa: '))
destinos = definir_destino()

empresa = Empresa(nombre, cantidad_colectivos, destinos)

# Menu

choice = 0
while choice != 3:
    menu()
    choice = int(input('Ingresa la opcion: '))
    if choice == 1:
    # Asignar Destino del colectivo
        destino = seleccionar_destino(destinos)
        try:
            colectivo = empresa.obtener_colectivo_libre()
            # colectivo.asignar_destino(destino) # no vamos a usar esto porque ya lo hace 
                                                 # empresa, pero sería igual de viable
            empresa.asignar_destino_a_colectivo(colectivo,destino)
            print('Se asigno el destino con exito')
        except NoHayColectivoLibreError as e:
            print(f'[!] Ha ocurrido un error: {e.msg}')
        except DestinoYaAsignadoError as e:
            print(f'[!] Ha ocurrido un error: {e.msg}')

    elif choice == 2:
        # Dar boleto
        destino = seleccionar_destino(destinos)
        try:
            boleto = empresa.generar_boleto(destino)
            print(f'Su asiento fue reservado: Colectivo: {boleto[0].numero} | Asiento: {boleto[1].numero}')
        except NoHayColectivoLibreError as e:
            print(f'[!] Ha ocurrido un error: {e.msg}')