"""
Construir un pequeño programa que convierta números binarios en enteros.

"""

def binario_decimales(lista):

    listainvertida = lista[::-1]
    posicion = 0
    Exp = 0
    resultado = 0

    for elemento in listainvertida:
        print(posicion ,"Posicion")
        Exp = (2**posicion)
        posicion += 1
        print(Exp ,"potencia")

        if elemento == 1:
            resultado += Exp
            print(resultado,"Resultado") 
                       
    return resultado

print(binario_decimales([1,1,1,1]))

""" Other way to do it """
# Se crea el metodo
def binario_entero(bynary):
    # Variable donde se almacena el valor total
    entero = 0
    # Recorreo los valores de la lista
    for digito in bynary:

        entero = entero*2 + int(digito)
    
    return entero

binario = input(" Por favor ingresa el nuero binario ")
print(binario_entero(binario))

    
    
"""
Construir un pequeño programa que convierta números binarios en enteros.

"""

    


