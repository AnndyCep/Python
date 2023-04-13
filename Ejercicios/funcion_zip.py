lista_uno = ["andres", "Ingred", "alba"]
lista_dos = ["Cepeda", "Herrera", "Herrera"]
"""Fucion ZIP
Concatena tuplas, de listas objetos
"""
# Variable donde se almacena las listas
# List / convierte el objeto zip a lista para que se pueda leer.

Concatenar_lista = list(zip(lista_uno,lista_dos))
print(Concatenar_lista)

# Podemos iterar sobre dos objetos iterables de forma simultanea
# dos elementos en el ciclo  "nombre , apellido ", 
# dentro de in zip(lista_uno,lista_dos):

for nombre , apellido in zip(lista_uno,lista_dos):
    print(nombre,apellido)


"""
Nos permite despaquetar los datos
"""
#  Se definen las variables "lista_uno_unzip, lista_dos_unzip"
#  Luego se les asigna la funcion ZIP, junto con el * para descadenar todas las variables  " zip(*Concatenar_lista)
#  print(lista_uno_unzip)"

lista_uno_unzip, lista_dos_unzip = zip(*Concatenar_lista)
print(lista_uno_unzip)
print(lista_dos_unzip)