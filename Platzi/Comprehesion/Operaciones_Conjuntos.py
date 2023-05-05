"""Union de conjuntos"""

set_a = { "Col", "Mex", "Bol"}
set_b = { "Pe","Bol"}

set_c = set_a.union(set_b)
print(set_c) # {'Bol', 'Mex', 'Pe', 'Col'} se unen los dos conjuntos
print(set_a | set_b) # {'Bol', 'Mex', 'Pe', 'Col'} genera la misma salida, pero la sintaxis es distinta

"""Intersection de elemtos"""
# Es decir que comparten el elemto en juntos conjuntos
set_c = set_a.intersection(set_b)
print(set_c)  # {'Bol'} 
print(set_a & set_b) # {'Bol'}

"""Diferencia, elimina los elementos del segundo conjunto """
set_c = set_a.difference(set_b)
print(set_c) # {'Col', 'Mex'} elimina los conjuntos del segundo conjunto 
print(set_a - set_b) # {'Col', 'Mex'} otra forma de la sixtazis

"""Diferencia simetrica"""
# Imprime los elemtos que no tienes nada en comunun  
set_c= set_b.symmetric_difference(set_b)
print(set_c) # {'Pe', 'Mex', 'Col'}
print(set_a ^ set_b) # {'Pe', 'Mex', 'Col'}
