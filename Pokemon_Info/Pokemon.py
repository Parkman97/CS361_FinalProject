import os
from clint.textui import colored

def controlFunction():
    from Main_menu import mainMenu
    from Search_PokemonMenu import searchPokemonMenu
    from Saved_Pokemon import savedPokemonList
    from Random_Pokemon import randompokemon
    from Display_PokemonName import displayPokemonName
    from Display_PokemonType import displayPokemonType 
    from Help_Menu import helpMenu
    from Updates import programUpdates 


    pokemonName = None 
    programRunning = True
    while programRunning:
        os.system('cls')
        main_input = mainMenu()
        os.system('cls')
        while main_input != 10:

            if main_input == 1:
                main_input = randompokemon()

            elif main_input == 2:
                main_input = searchPokemonMenu()

            elif main_input == 3:
                if  pokemonName == 1:
                    main_input = displayPokemonName(pokemonName)
                    pokemonName = None
                else:
                    main_input = displayPokemonName()

            elif main_input == 4:
                if pokemonName == 1:
                    main_input = displayPokemonType(pokemonName)
                    pokemonName = None
                else:
                    main_input = displayPokemonType()

            elif main_input == 5:
                result = savedPokemonList()
                if type(result) is tuple:
                    main_input = result[0]
                    pokemonName = result[1]
                else:
                    main_input = result

            elif main_input == 6:
                main_input = helpMenu()
                
            elif main_input == 7:
                main_input = programUpdates()

            elif main_input == 8:
                programRunning = False
                main_input = 10
                text = 'Thanks for using Poke-Display. We hope you come again!'
                i = 0
                for char in text:
                    print(getattr(colored, colored.COLORS[i])(f"{char}"), end="")
                    i += 1
                    if i == 7:
                        i = 0

if __name__ == "__main__":  
    os.system('cls')
    controlFunction()
    