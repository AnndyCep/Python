"""
 Escribir una función que tome un carácter y devuelva True si es una vocal, 
 de lo contrario devuelve False.

"""


def voval(letra):
    
    lista = ["a","e","i","o","u"]
    for elem in lista:
        if letra in lista:
            return True
    else:
        return False

print(voval("a"))