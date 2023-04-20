"""
Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. 
(Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es 
un muy buen ejercicio.

"""

def numeroMax(n1, n2):
    if n1 > n2:
        print(f"El numero mayor es {n1}")
    elif n1 > n2:
        print(f"El numero mayor es {n2}")
    else:
        print("Los numero son iguales")

numeroMax(3,1)

"""
Usando la funcion Max
"""
print(max(2,3))
