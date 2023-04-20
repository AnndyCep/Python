"""
Definir un histograma procedimiento() que tome una lista de números enteros e imprima un 
histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:
****
*********
*******
"""

def histograma(lista):
    for elemt in lista:
        print(elemt * " * ")

print(histograma([4,9,7]))