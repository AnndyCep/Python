"""
Escribir una función sum() y una función multip() que sumen y multipliquen
 respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4])
 debería devolver 10 y multip([1,2,3,4]) debería devolver 24.
"""

def suma(lista):
    contador = 0
    for elem in lista:
        contador += elem
    return contador

def mul(lista):
    contador = 1
    for elem in lista:
        contador = contador * elem
    return contador



print(suma([1,2,3,4]))
print(mul([1,2,3,4]))
