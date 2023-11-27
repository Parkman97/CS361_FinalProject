import os
from PIL import Image
from io import BytesIO  
import json
import time
from clint.textui import colored, puts
from Get_Image import get_image
from Sockets import api_socket
from Saved_Pokemon import savedPokemonList
from DataValidation import dataValidation

def displayPokemonName(pokemonName=None, pokemonDictionary=None):
    if pokemonName is None and pokemonDictionary is None:
        list_keys = ['types', 'id', 'abilities', 'locations', 'evolutions', 'base_stats']
        response_data = api_socket.recv(4096).decode()
        if "Error" in response_data:
            puts(colored.red('Incorrect Pokemon Name or Pokemon Name doesnt exist in database\n'))
            return 2
        dictionary_object = json.loads(response_data)
        for key in dictionary_object:
            pokemonName = key
            data = get_image(key)
            format_CLI(dictionary_object[key], list_keys)

    else:
        list_keys = ['types', 'id', 'abilities', 'forms', 'stats']
        data = get_image(pokemonName)
        pokemonDictionary = remove_keys(pokemonDictionary, ['url', 'is_hidden', 'slot'])
        format_CLI(pokemonDictionary, list_keys)

    try:
        img = Image.open(BytesIO(data))
        # Display the image
        img.show()

    except Exception as e:
        print(f"Error: {e}")

    validation = False
    while not validation:
        print('\nSelect a choice below: ')
        print('1. Search Pokemon/Type Menu')
        print('2. Get Random Pokemon')
        print('3. Save Pokemon')
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
        savedPokemonList((0, pokemonName))
        time.sleep(2)
        return 10
       

    if display_input == 4:
        return 10

    if display_input == 5:
        return 6
    
    
def remove_keys(data, keys_to_remove):
    if isinstance(data, list):
        return [remove_keys(item, keys_to_remove) for item in data]
    elif isinstance(data, dict):
        return {key: remove_keys(value, keys_to_remove) for key, value in data.items() if key not in keys_to_remove}
    else:
        return data
    
def format_CLI(dictionary, exclude_list):
    max_len = 0
    for key in dictionary:
        if key in exclude_list:
            if len(key) > max_len:
                max_len = len(key)

    for key in dictionary:
        if key in exclude_list:
            line_up = max_len - len(key)
            print(f'{key} {line_up * " "} |  {dictionary[key]}')