""" Un anagrama es un a palabras diferentes que contienen las mismas letras en distinto orden  """

# Este programa nos permite ingresar dos palabras de las cuales podremos sabes si son anagramas
def pal_anagrama(texto_uno, texto_dos):
    palabra_uno = sorted(texto_uno.lower())
    palabra_dos = sorted(texto_dos.lower())
    return palabra_uno == palabra_dos

print(pal_anagrama("ramo","mora"))
print(pal_anagrama("andres","Anndy"))

