from Figuras.prueba import area_cuadrado, perimetro_cuadrado, perimetro_figura,funcion_kwargs
from Figuras.circulo import area_circulo, perimetro_circulo


lado = 5

cuadrado = { 
    "lado": lado,
    "area": area_cuadrado(lado),
    "perimetro": perimetro_cuadrado(lado)
}
print(cuadrado)

radio = 3
circulo = {
    "radio": radio,
    "area": area_circulo(radio),
    "perimetro": perimetro_circulo(radio)
}

print(circulo)

perimetro = perimetro_figura(1,2,3,4)
print(perimetro)

Prueba = funcion_kwargs(nombre= "paco", apellido = "Botero")
print(Prueba)