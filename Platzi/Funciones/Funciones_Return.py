
# Se realiza la funcion con parametros
def calcular_volumen(alto, ancho,largo):
    # Se multiplica los valores, tambien se retorna el ancho, y el texto 
    return alto * ancho * largo, ancho, "Hola"

result,ancho, text= calcular_volumen(10,10,10)
# Se guarda en las variable, segun el orden que se retornan
print(result)
print(ancho)
print(text)