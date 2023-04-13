def funcion_map(numero):
    return numero**2
# Funcion que como parametro eleva el numero al cuadrado
lista_num = [1,2,3,4,5,6,7,8,9,10]
# Lista de num
lista_calcu = []
#Lista en la que me permite almacenar los
#datos iterados ya elevamos

# Itera cada elemento de la lista Num.
for elemento in lista_num:

# Guarda en la variable "Elevado" el numero elevado
#ya que llama a la funcion
    elevado = funcion_map(elemento)
    lista_calcu.append(elevado)
#Agrega a la lista vacia, el valor de la variable ya alevada
print(lista_calcu)

# Other example
#Usando la funcion Map, ya no es necesario realizar el
#proceso por el bucle
map_funcion = list(map(funcion_map , lista_num))
print(map_funcion)