import os
from DataValidation import dataValidation

def searchPokemonMenu():
    from Sockets import api_socket
    validation = False
    while not validation:
        print('Select a choice below:') 
        print('1. Search by Pokemon Name')
        print('2. Search By Pokemon Type')
        print('3. Main Menu ')
        print('4. Help Menu')
        searchParam = input('Enter your choice: ')
        

        result = dataValidation(1, 4, searchParam) 
        validation = result[0]
        if validation == True:
            searchParam = result[1]
        
    os.system('cls')

    if searchParam == 1:
        Name = True
        while Name:
            pokemonName = input('Enter the name of the Pokemon: ').lower()
            print('Are you sure you want to search for: ', pokemonName)
            print('\n1. Yes \n2. No\n')
            validate_input = input('Enter your choice here: ')
            result = dataValidation(1, 2, validate_input) 
            Name = result[0]
            if Name == True:
                validate_input= result[1]

            if validate_input == 1:
                Name = False
                api_socket.send((f"pokemon/{pokemonName}").encode('utf-8'))
                os.system('cls')
                return 3
            else:
                os.system('cls')

    if searchParam == 2:
        Type = True
        while Type:
            pokemonType = input('Enter the type of the Pokemon: ').lower()
            print('Are you sure you want to search for: ', pokemonType)
            print('\n1. Yes \n2. No\n')

            validate_input = input('Enter your choice here: ')
            result = dataValidation(1, 2, validate_input) 
            Name = result[0]
            if Name == True:
                validate_input= result[1]

            if validate_input == 1:
                Type = False
                os.system('cls')
                api_socket.send((f"type/{pokemonType}").encode('utf-8'))
                os.system('cls')
                return 4
            
            else:
                os.system('cls')
    
    if searchParam == 3:
        return 10

    if searchParam == 4:
        return 6