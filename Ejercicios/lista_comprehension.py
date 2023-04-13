lista = [1,2,3,4,5,6,7,8,9,10]
lista_cuadrados = []
for elemento in lista:
    dato = elemento**2
    lista_cuadrados.append(dato)
    print(" Cliclo for", lista_cuadrados)
                            
                             # Operacion / iterador dentro del ciclo / dentro de la lista
lista_comprehesion_otherExample = [num**2 for num in lista]
 # En resumen se ahorra la escritura de lineas de codigo 
print("Lista usando comprehesion", lista_comprehesion_otherExample)


"""Tambien podemos usar funciones dentro de la listas comprehension"""
def funcion_elevado2 (num):
    return num**2

def funcion_par (num):
    return num % 2 == 0
    
lista = [1,2,3,4,5,6,7,8,9,10]
lista_comprehesion_cuadrados =[funcion_elevado2(num) for num in lista]
print(lista_comprehesion_cuadrados)

lista_comprehesion_cuadrados_pares = [num**2 for num in lista if funcion_par(num)]
print(lista_comprehesion_cuadrados_pares)

lista_comprehesion_mas= [funcion_elevado2(num) if funcion_par(num) else 0 for num in lista]
print(lista_comprehesion_mas)

"""Podemos Crear un diccionario usando comprenhension"""
# Creamos un la lista
lista_num = [1,2,3,4,5,6,7,8,9,1,2,3,4]
# Se repiten caranteres en la lista
set_num = {num for num in lista_num if num % 2 == 0}
#Creamos un set comprehesion, con el fin de realizar el ciclo
#reutilizando codigo
#Num es el valor que retorna el ciclo/ inicia el ciclo for donde
#contamos con la codicion que deben ser pares
print(set_num)
# Se imprime la nuela lista

#Almacenamso una cadema en la variable
vocales = "aeiou"
# Creamos una variable donde se almacenara el diccionario con las
#mayusculas y niusculas.
set_diccionario = {vocal.lower(): vocal.upper() for vocal in vocales}
print(set_diccionario)