"""
Definir una función superposicion() que tome dos listas y devuelva True si tienen 
al menos 1 miembro en 
común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.
"""

def superposicion(Lis1, lis2):
    for elem in Lis1:
        for elen2 in lis2:
            if elem == elen2:
                return True
    else:
        return False


    """for elem in Lis1:
        if elem in lis2:
            return True
    else:
        return False"""

print(superposicion([1,2,3],[4,5,6]))