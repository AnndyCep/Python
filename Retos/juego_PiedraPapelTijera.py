import random

opcion = ("piedra","papel", "tijera")
round = 1
win_computer = 0
win_user= 0


while True :
    
    print("****" * 10)
    print( "Round :", round)
    print("****" * 10)

    selection_User = input("piedra, papel o tijera => ")
    selection_User= selection_User.lower()

    if not selection_User in selection_User:
        print("Opcion no valida")
    
    valor_Compu = random.choice(opcion)
    
    print("El valor que selecciono el User es : ", selection_User )
    print("El valor que selecciono la maquina es : ", valor_Compu )

    if valor_Compu == selection_User:
        print("Empate")
    if selection_User == "tijera":
        if valor_Compu == " papel ":
            print(" la tijera gana a papel ")
            print(f"gana el user ya que tiene {selection_User}")
            win_user= 0
            round += 1
        else:
            print(f"{valor_Compu} le gana a {selection_User}")
            print("la maquina gana")
            win_computer += 1
            round += 1
    if selection_User == "papel":
        if valor_Compu == " tijera ":
            print(" la tijera gana a papel ")
            print(f"gana la compu ya que tiene {valor_Compu}")
            win_computer += 1
            round += 1
        else:
            print(f"{valor_Compu} pierde con  {selection_User}")
            print("el user gana")
            win_user= 0
            round += 1
    if selection_User == "piedra":
        if valor_Compu == " tijera ":
            print(" la tijera pierde con roca ")
            print(f"gana  el user  ya que tiene {selection_User}")
            win_user= 0
            round += 1
        else:
            print(f"{valor_Compu} gana  con  {selection_User}")
            print("el compu gana")
            win_computer += 1
            round += 1
    
    if win_user == 2:
        print("El ganadamor es el User")
        break
    if win_computer ==2 :
        print("El ganadamor es el computador")
        break