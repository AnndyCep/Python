"""Podremos convertir las horas formato a 12 horas, a horas militares"""
def convertir_horas(texto):
    # Creo una variable, para almacenar el string el formato lista
    # La funcion split, me permite  dividir el string en la lista separador por el parametro ":"
    # eejemplo de salida ['12', '40 AM'] valor inicial "12:40 AM"
    hora_lista = texto.split(":")
   
    if texto[-2:].lower() == "pm":
        # Condicion que me permite filtrar los dos ultimos  valores del string, es decir si es PM, 
        # lo convierte a minusculas igualandolo a la condicion.
        if hora_lista [0] != "12":
            # Si la hora es distibta a 12, entonces le sumaremos  12 al valor que tenemos en el indice [0]
            hora_lista[0] = str(int(hora_lista[0])+12)
    else:
        if  hora_lista [0] == "12":
            # Si se cumple la condicion, solo cambiamos el valor de 12 por 00, ya que seria iniciando el dia
            hora_lista [0] = "00"
    convertir_horas = ":".join(hora_lista)
    # Creamos una variable para convertir las horas
    # Usanmos la funcion Join, para concatenar la lista a string separandolo por el parametro ":"

    return convertir_horas[:-2]

print(convertir_horas("12:40 AM"))
print(convertir_horas("04:59 PM"))
print(convertir_horas("10:00:00 PM"))

