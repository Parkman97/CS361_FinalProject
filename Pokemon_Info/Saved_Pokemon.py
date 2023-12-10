from Sockets import api_socket
from clint.textui import colored, puts
from DataValidation import dataValidation
import os
savedPokemons = []
savedTypes = []

def savedPokemonList(saved_item=None):
    os.system('cls')
    if saved_item is not None:
        if saved_item[0] == 0:
            if saved_item[1] not in savedPokemons:
                savedPokemons.append(saved_item[1])
        else:
            if saved_item[1] not in savedTypes:
                savedTypes.append(saved_item[1])
        print('List of saved Pokemon: ', savedPokemons)
        print('List of saved Types: ', savedTypes)
        input('\nEnter a value to continue: ')

    else:
        print(f'List of saved Pokemon: {savedPokemons}')
        print(f'List of saved Pokemon Types: {savedTypes}')

        validation = False
        while not validation:
            print('\n Select a choice below: ') 
            
            print('1. Display Pokemon from Saved List')
            print('2. Display Pokemon Type from Saved List')
            print('3. Remove a Pokemon')
            print('4. Remove a Pokemon Type')
            print('5. Help Menu')
            print('6. Main Menu')
            
            saved_input = input('Enter your number here: ')
            result = dataValidation(1, 6, saved_input) 
            validation = result[0]
            if validation == True:
                saved_input = result[1]
            
        os.system('cls')

        if saved_input == 1:
            
            if savedPokemons == []:
                puts(colored.red('No Pokemon saved yet.\n'))
                return 5
            
            validation = False
            while not validation:
                line_counter = 1
                print('Enter your choice of pokemon below\n')
                for pokemon in savedPokemons:
                    print(f'{line_counter}. {pokemon}')
                    line_counter += 1
            
                picked_pokemon = input('Enter your choice here: ')
                result = dataValidation(1, line_counter-1, picked_pokemon) 
                validation = result[0]
                if validation == True:
                    picked_pokemon = result[1]

            api_socket.send((f"pokemon/{savedPokemons[int(picked_pokemon)-1]}").encode('utf-8'))
            return (3,1)
        
        if saved_input == 2:

            line_counter = 1
            if savedTypes == []:
                puts(colored.red('No Pokemon type saved yet.\n'))
                return 5
            
            print('Enter your choice of pokemon type below\n')
            for types in savedTypes:
                print(f'{line_counter}. {types}')
                line_counter += 1
            
            picked_type = input('Enter your choice here: ')
            api_socket.send((f"type/{savedTypes[int(picked_type)-1]}").encode('utf-8'))
            return (4,1)

        if saved_input == 3:
            if savedPokemons == []:
                puts(colored.red('No Pokemon saved yet.\n'))
                return 5
        
            validation = False
            while not validation:
                line_counter = 1
                print('Enter the number of the Pokemon you wish to remove\n')
                for pokemon in savedPokemons:
                    print(f'{line_counter}. {pokemon}')
                    line_counter += 1
            
                picked_pokemon = input('Enter your choice here: ')
                result = dataValidation(1, line_counter-1, picked_pokemon) 
                validation = result[0]
                if validation == True:
                    picked_pokemon = result[1]

            savedPokemons.remove(savedPokemons[int(picked_pokemon) - 1])
            return 5

        if saved_input == 4:
            line_counter = 1
            if savedTypes == []:
                puts(colored.red('No Pokemon type saved yet.\n'))
                return 5
            
            print('Enter the number of Pokemon Type you wish to remove\n')
            for types in savedTypes:
                print(f'{line_counter}. {types}')
                line_counter += 1
            
            picked_type = input('Enter your choice here: ')
            savedTypes.remove(savedTypes[int(picked_type) - 1])

            return 5
        
        if saved_input == 5:
            return 6
        
        if saved_input == 6:
            return 10