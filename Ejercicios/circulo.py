def area_circulo (radio):
    return 3.14 * radio * radio

def perimetro_circulo (radio):
    return 3.14 * 2 * radio

radio = 3
circulo = {
    "radio": radio,
    "area": area_circulo(radio),
    "perimetro": perimetro_circulo(radio)
}
print(circulo)