import os
import json
from Sockets import api_socket
import time
from clint.textui import colored, puts
from Saved_Pokemon import savedPokemonList
from DataValidation import dataValidation
from DataFormatting import dataFormatting

def displayPokemonType(pokemonType=None):
    saved_menu = False
    
    if pokemonType == 1:
        saved_menu = True

    key_list = []
    response_data = api_socket.recv(4096).decode()
    if "Error" in response_data:
            puts(colored.red('Incorrect Pokemon Type or Pokemon Type doesnt exist in database\n'))
            return 2
    dictionary_object = json.loads(response_data)
    pop_keys = dictionary_object['damage_relations']
    for keys in pop_keys:
        if pop_keys[keys] == []:
            key_list.append(keys)
    for i in key_list:
        dictionary_object['damage_relations'].pop(i)

    dataFormatting('type', dictionary_object)

    if saved_menu is True:
        return 5
    
    validation = False
    while not validation:
        print('\nSelect a choice below: ')
        print('1. Search Pokemon/Type Menu')
        print('2. Get Random Pokemon')
        print('3. Save Type')
        print('4. Main Menu')
        print('5. Help Menu')
        
        display_input = input('Enter your number here: ')
        result = dataValidation(1, 5, display_input) 
        validation = result[0]
        if validation == True:
            display_input = result[1]

    os.system('cls')
    
    if display_input == 1:
        return 2
    
    if display_input == 2:
        return 1

    if display_input == 3:
        puts(colored.red('\n Pokemon has been saved'))
        savedPokemonList((1, dictionary_object['name']))
        time.sleep(2)
        return 10

    if display_input == 4:
        return 10

    if display_input == 5:
        return 6