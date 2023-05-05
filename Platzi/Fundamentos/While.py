
# Mienstras la condicion se cumpla se repetira lo que hay en la condicion.
count = 0

while count <=10:
    print(count)
    count += 1

"""
Other way to do it

"""

while count <20:
    count += 1
    if count == 15:
        break
    # Se rompe el ciclo ya que se cumple la condicion.
    print(count)

"""
Other way to do it

"""
valor = 0
while valor <20:
    valor += 1
    if valor < 15:
        continue
    # Continue salta a la sigiente iteracion.
    print(count)