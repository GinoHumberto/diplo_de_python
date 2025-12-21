from empresa import Empresa
from salas import Sala
from database import Database
from entrada import Entrada

for i in range(4):
    Empresa().agregar_pelicula()

for i in range(5):
    Entrada().vender_entrada()