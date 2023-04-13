def polindroma(texto):
    texto_minuscula = texto.lower()
    texto_sinespacios = texto_minuscula.replace(" ", "")
    return texto_sinespacios == texto_sinespacios[::-1]

print(polindroma("Anita lava la tina"))
print(polindroma("Polindromo"))
"""Este programa permite validar si una palabra es polindroma"""

def polindroma(tecto):
    minusculas = tecto.lower()
    sin_espacios = minusculas.replace(" ", "")
    return sin_espacios == sin_espacios[::-1]

print(polindroma("Anita lava la tina"))
print(polindroma("Andres"))

def letra_repetida(texto):
    minusculas = texto.lower()
    sin_espacios = minusculas.replace(" ", "")
    lista_vacia = []
    for letter in sin_espacios:
        if letter in lista_vacia:
            return letter
        else:
            lista_vacia.append(letter)
    return None
 
print(letra_repetida("Hola"))
print(letra_repetida("Hola Mundo"))

def letra_repetidas(texto):
    texto_minusculas = texto.lower()
    sin_espacios = texto_minusculas.replace(" ", "")
    lista_vacia = []
    for letra in sin_espacios:
        if letra in lista_vacia:
            return print(f" La palabra { texto } tiene la letra {letra} repetida")
        else:
            lista_vacia.append(letra)
    return print(f" la palabra {texto} no tiene palabras repetidas" )

print(letra_repetidas("Hola"))
print(letra_repetidas("Hola mundo"))

def Pol(tex):
    min = tex.lower()
    espacios = min.replace(" ", "")
    if espacios == espacios[::-1]:
        return print(f" La palabra { tex } es polindroma")
    return print(f" La palabra { tex } no  polindroma")

print(Pol("Anita lava la tina"))
print(Pol("Hola"))


def letrarepetida(tex):
    min= tex.lower()
    espacios = min.replace(" ", "")
    vacia = []
    for letra in espacios:
        if letra in vacia:
            return letra
        else:
            vacia.append(letra)
    return tex

print(letrarepetida("Hola"))
print(letrarepetida("Hola mundo"))