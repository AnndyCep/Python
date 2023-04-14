import re # Regular Expresion,  libreria que nos permite eliminar caracteres especiales, la importamos

def cadena_sslugify(texto):
    slug = (texto
        .lower() # Nos permite convertir el texto en minusculas
        .strip() # Nos permite eliminar los espacios que existan al inicio o al final del texto
        .replace(" ", "-")  # Nos permite remplazar los espacios por giones
    )
    slug = re.sub("[^\w\-]", "", slug) 
    # Modificacmos la variable, para almacenar los datos sin caracteres
    # Usamos la funcion (re) junto con junto con (sub) que nos permite remplazar un conjunto de caracteres
    # en la expresion,  (re.sub("[^\w\-]", "", slug))
    # La primera condicion, indica que caracteres quiere remplazar, 
    # como segunda porque las quieres cambiar, en este caso ("") comillas vacias, 
    # Tercer argumento, el texto del cual se haran las modificaciones (slug)

    return slug

print(cadena_sslugify("texto% con caracteres$# especiales!"))
print(cadena_sslugify("Ohter ex5## ampel "))

