
dictinary = {}
for i in range(1,6):
    dictinary[i] = i * 2
print(dictinary) # {1: 2, 2: 4, 3: 6, 4: 8, 5: 10}

""" listcomprehension """
      # Llave / valor 
dic_v1 = {i: i * 2 for i in range(1,6)}
print(dic_v1) # {1: 2, 2: 4, 3: 6, 4: 8, 5: 10}

"""other way to do it  """
import random
contries = ["Col","Mex","Pe","Arg"]
population = {}
# Se itera la posicion en la lista
for country in contries:
    # Se asigna el pais como clave y numero aleatorio como valor
    population[country] = random.randint(1,50)

print(population) # {'Col': 19, 'Mex': 12, 'Pe': 30, 'Arg': 36}

"""Asignado list comprehension con diccionario"""
population_v2 = { key : random.randint(1,20) for key in contries}
print(population_v2) #  {'Col': 10, 'Mex': 15, 'Pe': 1, 'Arg': 7}

""" Conatenar listas """
name = [ "Andres", " Ingrid ","Alba"]
age = [25 , 29, 45]
# Se concatena las dos listas dejnado el mismo indice 
print(list(zip(name,age)))  # [('Andres', 25), (' Ingrid ', 29), ('Alba', 45)]

"""List comprehension concatenar listas"""
        # llave / valor  
nwe_lista = { name : age for (name, age) in zip(name, age)}
# Se almacena como un diccionary 
print(nwe_lista) #  {'Andres': 25, ' Ingrid ': 29, 'Alba': 45}