"""
Ejercicio 1
La función max() del ejercicio 1 (primera parte) 
y la función max_de_tres() del ejercicio 2 (primera parte), 
solo van a funcionar para 2 o 3 números. Supongamos que
 tenemos mas de 3 números o no sabemos cuantos números son.
 Escribir una función max_in_list() 
que tome una lista de números y devuelva el mas grande
"""

def max_in_list(list):
    
    mayor = list[0]

    for elemento  in range(1, len(list)):
        if list[elemento] > mayor :
            mayor = list[elemento]
    
    return mayor

listaNueva = [1,8,4,7,6,4,5,2,1,4]
print(max_in_list(listaNueva))


"""
Ejercicio 1
La función max() del ejercicio 1 (primera parte) 
y la función max_de_tres() del ejercicio 2 (primera parte), 
solo van a funcionar para 2 o 3 números. Supongamos que
 tenemos mas de 3 números o no sabemos cuantos números son.
 Escribir una función max_in_list() 
que tome una lista de números y devuelva el mas grande
"""

