"""
Las propiedades de conjuntos, a un conjunto se le puede modificar,
 sin embargo los conjuntos, los elementos no tienen orden en especifico y no se pueden duplicar

"""

set_contries = {
    "Colombia",
    "Mexico",
    "Peru"
}

print(set_contries) # Colombia, Peru, Mexico
print(type(set_contries)) # Class set

"""
Se pueden con distintos tipos de datos, pero recuerda que no se pueden repetir
"""

""" Manera explicita de crear el conjunto """
set_tyoes = {
    "Colombia",
    1,
    1,
    False,
    12.2
} 

print(set_tyoes) # Colombia, Peru, Mexico
print(type(set_tyoes)) # Class set

""" Otra manera de crear un conjunto desde otra estructura """

set_from_string = set("Hoolaa") 
print(set_from_string) # {'o', 'l', 'H', 'a'} resultado de la impresion

set_from_tuplas = set(("abc","def","ghi","as","abc"))
print(set_from_tuplas) # {'def', 'abc', 'ghi', 'as'} resutado de la impresion

lista = [1,2,3,4,5,1,2,3]
set_from_listas = set(lista)
print(set_from_listas) # {1, 2, 3, 4, 5} impresion de la lista sin duplicados
print(type(set_from_listas)) # Class set, ingresa como lista pero retorna conjunto set
numeros_unicos = list(set_from_listas) # Se trasforman los numeros unicos a listas de nuevo

 


