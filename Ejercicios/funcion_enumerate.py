Mi_lista = ["andres", "cepeda", "herrera"]
for indice, nombre in enumerate(Mi_lista):
    print(indice,nombre)
# other example
# Si queremos imprimir la lista junto con sus indices
nombre_enumerados = enumerate(Mi_lista)
print(list(nombre_enumerados))
# No olvidar que se debe parsear a tipo List para que
# Se permita leer el dato en consola
