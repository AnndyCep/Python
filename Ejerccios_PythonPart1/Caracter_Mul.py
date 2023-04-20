"""
Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter 
multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".
"""

def generar_n_caractereres(caracter, n):
    #valor = (caracter * n)
    #return valor
    valor = caracter
    for i in range(1,n):
        valor += caracter
    return valor


print(generar_n_caractereres("x", 5))