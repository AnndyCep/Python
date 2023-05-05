import random # Funcion Ramdom

print("""
      [ 🤖 Bienvenido al juego Piedra, Papel o tijera 🙋]
                  >>> Ingresa una opción <<<
      """) # Bienvenida al juego


def choose_options():
    """
    The function allows the user to choose between rock, paper, or scissors and returns the user's
    choice and a randomly generated computer choice.
    :return: a tuple with the user's option and the computer's option. If the user's option is not
    valid, the function returns None for both options.
    """

    options = ('piedra', 'papel', 'tijera')
    user_option = input('>>> Piedra, papel o tijera => ').lower()
   
    if not user_option in options:
        print('Esa opción no es valida')
        
        return None, None 
    
    computer_option = random.choice(options)

    print('User option => ', user_option)
    print('Computer option => ', computer_option)
    return user_option, computer_option


def check_rules(user_option, computer_option, user_wins, computer_wins):
    """
    The function takes in user and computer options, checks the rules of the game, and returns the
    updated number of wins for both the user and computer.
    
    :param user_option: The option chosen by the user (either "piedra", "papel", or "tijera")
    :param computer_option: The option that the computer chooses (either "piedra", "papel", or "tijera")
    :param user_wins: an integer representing the number of times the user has won the game
    :param computer_wins: The number of times the computer has won so far in the game
    :return: the updated values of the variables `user_wins` and `computer_wins`.
    
    """
    
    if user_option == computer_option:
        print('Empate!\n')
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('🪨 Piedra gana a tijera ✂️')
            print('¡User gana!\n')
            user_wins += 1
        else:
            print('📄 Papel gana a piedra 🪨')
            print('¡Computer gana!\n')
            computer_wins += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('📄 Papel gana a piedra 🪨')
            print('¡User gana!\n')
            user_wins += 1
        else:
            print('✂️ Tijera gana a papel 📄')
            print('¡Computer gana!\n')
            computer_wins += 1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('✂️ Tijera gana a papel 📄')
            print('¡User gana!\n')
            user_wins += 1
        else:
            print('🪨 Piedra gana a tijera ✂️')
            print('¡Computer gana!\n')
            computer_wins += 1
            
    return user_wins, computer_wins


def check_winner(user_wins, computer_wins):
    """
    The function checks if either the user or computer has won three times and prints the winner.
    
    :param user_wins: The number of times the user has won in a game
    :param computer_wins: The number of times the computer has won in a game
    """
    
    print(f'''
    🤖 Computer wins: {computer_wins}
    🙋 User wins: {user_wins}
            ''')
    
    if user_wins == 3:
        print('🎖️ El ganador es User 🎖️')
        exit()
        
    if computer_wins == 3:
        print('🎖️ El ganador es Computer 🎖️')
        exit()


def run_game():
    """
    This function runs a game where the user and computer choose options and their wins are tracked
    until a winner is determined.
    """
    
    computer_wins = 0 
    user_wins = 0
    rounds = 1

    while True:
        print('***' * 10)
        print('Round ', rounds)
        print('***' * 10)

        rounds += 1
              
        user_option, computer_option = choose_options()
        user_wins, computer_wins = check_rules(user_option, computer_option,user_wins, computer_wins)
        check_winner(user_wins, computer_wins) 
        
                    
run_game()
    
    
    