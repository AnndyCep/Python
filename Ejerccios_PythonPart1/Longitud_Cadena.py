"""
 Definir una función que calcule la longitud de una lista o una cadena dada.
   (Es cierto que python tiene la función len() incorporada,
   pero escribirla por nosotros mismos resulta un muy buen ejercicio.
"""

def longitud_lista(lista):
    contador = 0
    for elemt in lista:
        contador += 1
    return contador     
    

print(longitud_lista([1,2,3,4,5,6]))
print(longitud_lista(["Andres","Baby"]))
print(longitud_lista("Andres"))