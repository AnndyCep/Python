def parentesis_desbalanceados(texto):
    
    balanceado = 0

    for parentesis in texto:
        if parentesis == "(":
            balanceado += 1
        elif parentesis == ")":
            balanceado -= 1
            if balanceado < 0:
               return print(" No esta balanceado", texto)
            
    return balanceado == 0

print(parentesis_desbalanceados("()()()"))
print(parentesis_desbalanceados("())()"))
print(parentesis_desbalanceados(")()()"))