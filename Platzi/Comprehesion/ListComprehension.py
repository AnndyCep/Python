

lista = []
for elemto in range(1, 11):
    lista.append(elemto)

print(lista) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

""" ListComprehension"""

lista_v2 = [element * 2 for element in range(1 , 11)]
print(lista_v2) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

""" other way to do it """
lista_v3 = []
for i in range(1, 101):
    if i % 2 == 0:
        lista_v3.append(i)
print(lista_v3)

""" ListComprehension"""

lista_v4 = [i for i in range(1,101) if i % 2 == 0]
print(lista_v4)