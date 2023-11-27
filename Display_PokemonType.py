import os
from PIL import Image
from io import BytesIO  
import json
from Sockets import api_socket
from Get_Image import get_image
import time
from clint.textui import colored, puts
from Saved_Pokemon import savedPokemonList
from DataValidation import dataValidation

def displayPokemonType():
    key_list = []
    response_data = api_socket.recv(4096).decode()
    if "Error" in response_data:
            puts(colored.red('Incorrect Pokemon Type or Pokemon Type doesnt exist in database\n'))
            return 2
    dictionary_object = json.loads(response_data)
    pokemonName = dictionary_object['pokemon'][0]
    pop_keys = dictionary_object['damage_relations']
    for keys in pop_keys:
        if pop_keys[keys] == []:
            key_list.append(keys)
    for i in key_list:
        dictionary_object['damage_relations'].pop(i)
    data = get_image(pokemonName)
    format_CLI(dictionary_object)
    
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

def format_CLI(dictionary):
    max_len = 0
    for key in dictionary:
        if len(key) > max_len:
            max_len = len(key)

    for key in dictionary:
        line_up = max_len - len(key)
        print(f'{key} {line_up * " "} |  {dictionary[key]}')