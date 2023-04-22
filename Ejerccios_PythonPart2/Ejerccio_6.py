"""
Escribir un pequeño programa donde:
- Se ingresa el año en curso.
- Se ingresa el nombre y el año de nacimiento de tres personas.
- Se calcula cuántos años cumplirán durante el año en curso.
- Se imprime en pantalla.
"""

def fecha_nacimiento():

    fechaActual = int(input(" Dime cual es el año es curso"))
    datos = []
    for i in range(3):
        name = input (" Ingrese el nombre y apellido ")
        date_birday = int(input(" Año de nacimiento de {}: ".format(name)))
        age = (fechaActual - date_birday )
        datos.append((name,age))
        print(datos)
    
    for peple in datos:
        print("{} cumplira {} años durante el año en curso".format(peple[0],peple[1]))


fecha_nacimiento()














