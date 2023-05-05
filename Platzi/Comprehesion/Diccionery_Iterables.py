""" Dictionary Comprehension condicionales """
import random
lista_paises = ["Col","Ven","Ecu","Pa"]
        #           Clave / valor            se itera cada pais en la lista de paises   
populations = { contries : random.randint(1,50) for contries in lista_paises}
print(populations) # resultado {'Col': 42, 'Ven': 40, 'Ecu': 8, 'Pa': 36}

"""Ahora se realiza con una condicion con list comprehension """
         # Clave / valor --- 
resul = { countries : population for (countries, population) in populations.items() if population >= 20}
print(resul)


""" Practico """
"""Trasformar el siguiente texto a un dicionario, donde la clave sera la vocal, y su valor sera la misma vocal
pero en mayuscula
"""

tex = "Hola soy Andres"
#Variable- Clave / valor - itera cada letra en tex / condicion si vocal esta dentro de "aeiou"
dicti = { v : v.upper() for v in tex if v in "aeiou"}
print(dicti) # Se imprime {'o': 'O', 'a': 'A', 'e': 'E'}




