"""
Ejercicio 4
Escribir un programa que le diga al usuario que ingrese una cadena.
 El programa tiene que evaluar la cadena y decir cuantas letras mayúsculas tiene.
"""

def mencion_Mayus():

    palabra = input("Ingrese una palabra")
    mayusculas = 0

    for letra in palabra:
        #Insuper es una funcion que nos permite saber las muyusculas 
        if letra.isupper():
            mayusculas += 1
    
    print(f"Hola la palabra es : {palabra} tiene {mayusculas} mayusculas")


mencion_Mayus() 




"""
Ejercicio 4
Escribir un programa que le diga al usuario que ingrese una cadena.
 El programa tiene que evaluar la cadena y decir cuantas letras mayúsculas tiene.
"""
