"""
Escribir una función filtrar_palabras() que tome una lista 
de palabras y un entero n, y devuelva las palabras que tengan mas de n caracteres.

"""

def filtrar_palabras(lista, n):
    
    palabras_filtradas = [palabras for palabras in lista if len(palabras) > n]

    """for palabra in lista:
        if len(palabra) > n:
                    
         palabras_filtradas.append(palabra)
    """
    return palabras_filtradas

print(filtrar_palabras(["Andres","Ta","Liss","Alba"],3))









"""
Escribir una función filtrar_palabras() que tome una lista 
de palabras y un entero n, y devuelva las palabras que tengan mas de n caracteres.

"""
