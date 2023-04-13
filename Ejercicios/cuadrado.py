def area_cuadrado (lado):
   # Calcular el area del cuadrado
    return lado * lado

def perimetro_cuadrado(lado):
   # Calcular el perimetro del cuadrado
    return    lado * 4

lado = 5

cuadrado = { 
    "lado": lado,
    "area": area_cuadrado(lado),
    "perimetro": perimetro_cuadrado(lado)
}
print(cuadrado)