def lista_numeros(lista_numeros):
    # Creamos nuestra funcion donde recibe una lista
    pares =[]
    impares = []
    # Creamos dos lista vacias
    for numeros in lista_numeros:
        # Iteramos cada numero dentro de la lista numeros
        if numeros %2 == 0:
            # si cada numero es par lo add a la lista pares
            pares.append(numeros)
        else:
            impares.append(numeros)
            #Si no se añanade a la lista impates
    return pares,impares
    # retornamos la lista pares e impares

print(lista_numeros([1,2,3,4,5,6,7,8,9]))

# Otro ejemplo de numeros pares usando la funcion lambda

lista_numeros = [1,2,3,4,5,6,7,8,9,10]
# Variable en la que se guarda el valor
lista_pares = list(filter(lambda numero : numero %2 == 0, lista_numeros))
# List / es para convertir de tipo objeto a lista
# Filter es la funcion que nos permite filtrar, la primera expreion es la funcion landa "lambda numero : numero %2 == 0",
# y la segunda es lista de numeros "lista_numeros".
print(lista_pares)

# Este programa permite imprimir la lista de numeros pares
# para impartes solo se cambia el 1 por un o
for elemento in lista_numeros:
    if elemento % 2 == 1:
        continue
    print(elemento)