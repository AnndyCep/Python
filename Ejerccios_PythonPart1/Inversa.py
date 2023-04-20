"""
Definir una función inversa() que calcule la inversión de una cadena.
 Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"
"""
def inversa(cadena):
    nueva_Inv = cadena[::-1]
    return nueva_Inv

def polindroma(cadena):
    nuevacadena = inversa(cadena)
    return nuevacadena == cadena

print(inversa("odnaborp yotse"))
print(polindroma("radar"))