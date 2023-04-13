def palabra_polindroma(texto):
    minusculas = texto.lower()
    palabra_sin_espacios = minusculas.replace(" ", "")
    return palabra_sin_espacios == palabra_sin_espacios[::-1]

print(palabra_polindroma("Hola"))
print(palabra_polindroma("Anita lava la tina"))
