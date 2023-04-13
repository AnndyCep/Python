def funcion_repeated_letters(texto):
    sin_mayusculas = texto.lower()
    sin_espacios = sin_mayusculas.replace(" ", "")
    vacia =[]
    for letter in sin_espacios:
        if letter in vacia:
            return letter
        else:
            vacia.append(letter)
    return None

    

print(funcion_repeated_letters("Hola"))
print(funcion_repeated_letters("Hola Mundo"))