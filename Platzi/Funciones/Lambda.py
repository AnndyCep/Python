## Lambda funtion es otra forma de sintaxis de una funcion
"""Funcion normal"""
def incremento(n):
    return n + 1

resultado = incremento(1)
print(resultado) # 2

"""Lambda funtion"""
# Nombre de variable / lambda + argumento / retorno
Increment = lambda x : x + 1

resultado2 = Increment(2)
print(resultado2) # 3

"""Funcion Lambda concatenada """
# nombre de la varible / parametros de la funcion donde le enviamos una funcion  / returno
# The code defines a lambda function called `FuntionLabda` that takes two arguments, `x` and `funt`.
# It then returns the sum of `x` and the result of calling the function `funt` with `x` as its
# argument.

FuntionLabda = lambda x , funt : x + funt(x)

result = FuntionLabda(2, Increment)
print(result) # 5