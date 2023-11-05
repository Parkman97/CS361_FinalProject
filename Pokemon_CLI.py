import os 
from clint.textui import prompt, validators, colored, puts
import time


def mainMenu():
    print('Welcome to poke-Display! From the options below please enter the corresponding number and hit enter! \n')
    print('1. Display Random Pokemon (Recommended) ')
    print('2. Search By Pokemon Name or Type')
    print('3. Saved Pokemon List')
    print('4. Help')
    print('5. Update Notes')
    print('6. Exit')
    user_input = int(input('Enter the number here: '))
    return user_input

def displayMenu():
    print('Pokemon Name: ')
    print('Pokemon Type: ')
    print('Pokemon Nature: ')
    print('Pokemon Abilities: ')

    print('\nSelect a choice below: ')
    print('1. Search for another Pokemon')
    print('2. Main Menu')
    print('3. Save Pokemon')
    print('4. Help Menu')
    display_input = int(input('Enter your number here: '))

    if display_input == 1:
        os.system('cls')
        searchPokemonMenu()

    if display_input == 2:
        controlFunction()

    if display_input == 3:
        puts(colored.red('\n Pokemon has been saved'))
        time.sleep(2)

    if display_input == 4:
        helpMenu()

def savedPokemonList():
    print('Saved Pokemon')
    savedPokemon = []
    print('List of saved Pokemon: ', savedPokemon)

    print('\n Select a choice below: ') 
    
    print('1. Help Menu')
    print('2. Main Menu')
    saved_input = int(input('Enter your choice here:'))

    if saved_input == 1:
        helpMenu()

def searchPokemonMenu():
    print('Select a choice below:') 
    print('1. Search by Pokemon Name')
    print('2. Search By Pokemon Type')
    print('3. Main Menu ')
    searchParam = int(input('Enter your choice: '))
    os.system('cls')

    if searchParam == 1:
        Name = True
        while Name:
            pokemonName = input('Enter the name of the Pokemon: ')
            print('Are you sure you want to search for: ', pokemonName)
            print('\n1. Yes \n2. No\n')
            validate_input = int(input('Enter your choice here: '))
            if validate_input == 1:
                Name = False
                print('Sends data to partners microservice')
                os.system('cls')
                displayMenu()

    if searchParam == 2:
        Type = True
        pokemon_type = []
        while Type:
            pokemonType = input('Enter the type of the Pokemon: ')
            print('Are you sure you want to search for: ', pokemonType)
            print('\n1. Yes \n2. No\n')
            validate_input = int(input('Enter your choice here: '))
            if validate_input == 1:
                Type = False
                os.system('cls')
                print('List of pokemon with that type will be displayed', pokemon_type)
                input('User will be able to select a pokemon from the list. Hit any key to move on: ')
                os.system('cls')
                displayMenu()

    if searchParam == 3:
        controlFunction()


def programEnd():
    print('Will utilize partners microservice later')
    print('Thanks for using Poke-Display. We hope you come again!')

def programUpdates():
    read_file = open("UpdateNotes.txt", "r")
    for text in read_file:
        print(text)
    puts(colored.red('\n Enter any key to return to the main menu:'))
    input()
    

def helpMenu():
    os.system('cls')
    read_file = open("HelpMenu.txt", "r")
    for line in read_file:
        print(line)
    puts(colored.red('\n Enter any key to return to the main menu:'))
    input()

def controlFunction():
    programRunning = True
    while programRunning:
        os.system('cls')
        main_input = mainMenu()
        os.system('cls')
        if main_input == 1:
            displayMenu()
        elif main_input == 2:
            searchPokemonMenu()
        elif main_input == 3:
            savedPokemonList()
        elif main_input == 4:
            helpMenu()
        elif main_input == 5:
            programUpdates()
        elif main_input == 6:
            programEnd()
            programRunning = False


if __name__ == "__main__":  
    os.system('cls')
    controlFunction()
    