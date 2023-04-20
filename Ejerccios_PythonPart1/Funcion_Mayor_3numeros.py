"""
Definir una función max_de_tres(),
 que tome tres números como argumentos y devuelva el mayor de ellos.
"""
def max_de_tres(n1,n2,n3):
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n3 and n2 > n1:
        return n2
    elif n3 > n2 and n3 > n1:
        return n3
    
print(max_de_tres(3,2,7))

"""
Otra forma de realizar el proceso mediante una lista
"""
def proceso_lista(lista):
    mayor = lista[0]
    menor = lista[0]
    for indice in range(1,len(lista)):
        if lista[indice] > mayor:
            mayor = lista[indice]
        if lista[indice] < menor:
            menor = lista[indice]
    medio = (mayor / 2)

    print(f" El numero mayor es {mayor} \n")
    print(f" El numero menor es {menor} \n")
    print(f" El numero medio es {medio} \n")

print(proceso_lista([1,2,3,4,5,6]))
