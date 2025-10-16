archi1=open('datos.txt','w')
archi1.write('Hola mundo\n')
archi1.write('Hola mundo1\n')
archi1.write('Hola mundo2\n')
archi1.close()

# archi1=open("datos.txt","r")
# contenido=archi1.read()
# print(contenido)
# archi1.close()

archi1=open("datos.txt","r")
linea=archi1.readline()
while linea!='':
    print(linea, end='')
    linea=archi1.readline()
archi1.close()