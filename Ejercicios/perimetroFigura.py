def perimetro_figura(*args):
    print(args)
    perimetro = 0
    for lado in args:
        perimetro += lado
    return perimetro

perimetro = perimetro_figura(1,2,3,4)
print(perimetro)