"""
Escribir una función mas_larga() que tome una lista de palabras y devuelva la mas larga.
"""
# Creamos una funcion llamada mas:larga
def mas_larga(lista):
    # Creamos una variable con el nombre paralabra... para hacer la prueba logica
    palabra_mas_larga = ""
    # Iteramos para palabara dentro del arreglo
    for palabra in lista:
        # La longitud de la palabra es mayor a la labra asignada
        if len(palabra) > len(palabra_mas_larga):
            # Como es verdadero se asigna el nuevo valor
            palabra_mas_larga = palabra
    # Se retorna el valor
    return palabra_mas_larga

listaNombre =  ["Andresss","Tatiana", "Fersasasasa", "Rodri"]
print(mas_larga(listaNombre))




"""
scribir una función mas_larga() que tome una lista de palabras y devuelva la mas larga.
"""

