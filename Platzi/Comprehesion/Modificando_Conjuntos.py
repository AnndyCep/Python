

set_contries = {"Col","Mex","Bol"}

size = len(set_contries) #Funcion para ver la cantidad de elementos en un conjunto
print(size) # Resultado es 3 

print("col" in set_contries) # Devuelve un boleano dependiendo de la condicion logica False/True

"""Agregando un elemento al conjunto"""
set_contries.add("Pe")
print(set_contries)

"""Actualizar un numero elemneto"""
set_contries.update({"Arg", "Ecu", "Pe"})
print(set_contries)

"""Como remover elementos de alli del conjunto"""
set_contries.remove("Col")
print(set_contries)
set_contries.remove("Arg")
print(set_contries)

"""Eliminar todo el conjunto de datos"""
set_contries.clear()
print(set_contries)
print(len(set_contries))