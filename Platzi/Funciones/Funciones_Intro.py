# se crea  una funcion, para sumar el total de un numero de datos
def suma_rango(nim, max):
    suma = 0
    for x in range(nim, max):
        suma += x
        # Se suma en la variable el total de las iteraciones
    return suma

print(suma_rango(20, 30)) # Se imprime el total de 245
print(suma_rango(1,10)) # Total de 45