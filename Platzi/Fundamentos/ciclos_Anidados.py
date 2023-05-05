"""
Lo cilcos permiten iterar de forma mas sencilla, matrices, forma de representar datos, representar tablas.

"""

matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]
# Tabla de filar y columnas

print(matriz[0]) # posicion
print(matriz[0][1]) # A nivel de coordenadas

"""
Podemos recorrerlo de forma distinra con un for
"""

for row in matriz: # iteramos la  fila  en la matriz
    print(row)  # imprimimos toda la fila
    for column in row: # Iteramos en la columna
        print(column) # imprimimaos la columna de la fila