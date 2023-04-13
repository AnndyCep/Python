def funcion_repeated_letters(texto):
    # se crea una variable para almacenar la palabra en minuscula
    sin_mayusculas = texto.lower()
    # se crea una variable para almecenar la palabra sin espacios
    sin_espacios = sin_mayusculas.replace(" ", "")
    # Creamos una lista vacia que nos permite almacer los datos
    vacia =[]
    for letter in sin_espacios:
        # realizamos un ciclo para iterar para letra en la palabra sin espacion
        if letter in vacia:
            # condicion que nos permite saber si la letra se retipe
            return letter #retorna la primera letra repetida
        else:
            vacia.append(letter) # añade la letra a la lista vacia
    return None # retorna None si no se peten letras

    

print(funcion_repeated_letters("Hola"))
print(funcion_repeated_letters("Hola Mundo"))