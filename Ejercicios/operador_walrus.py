"""Con el operador walrus nos permite asignar un valor a una variable miestas se evalua 
como expresion"""

def fucion_cuadrado(num):
    return num **2

lista_numeros =  [1,2,3,4,5,6,7,8,9,10]
lista_pares = []

for num in lista_numeros:
    #cuadrado = fucion_cuadrado(num) / escritura coloquial
    if (cuadrado:=fucion_cuadrado(num) ) % 2 == 0:
        # Con el operador Walrus, nos permite ralizar todo el proceso en condicion
        # Asignandole el valor de la funcion directamente en cuandrado.
        lista_pares.append(cuadrado)
        print(f"El numero {num}  el cuadrado es {cuadrado}  y este es par")
    else:
        print(f"El numero {num}  el cuadrado es {cuadrado}  y este es impar")

print(lista_pares)

#Con la lista comprehesion realizamos el mismo proceso, con menos lineas de codigo
Lista_comprehesion = [cuadrado for num in lista_numeros if (cuadrado := fucion_cuadrado(num)) % 2 ==0]
            # valor resultado / Iterador en la lista / Condicion - operador Walrus que se almacena en la variable- Condicion par
print(Lista_comprehesion)