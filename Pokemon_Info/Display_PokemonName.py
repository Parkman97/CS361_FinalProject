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
from DataFormatting import dataFormatting

def displayPokemonName(pokemonName=None):
    saved_menu = False

    if pokemonName == 1:
        saved_menu = True
        
    response_data = api_socket.recv(4096).decode()
    if "Error" in response_data:
        puts(colored.red('Incorrect Pokemon Name or Pokemon Name doesnt exist in database\n'))
        return 2
    dictionary_object = json.loads(response_data)
    for key in dictionary_object:
        pokemonName = key
        data = get_image(key)
        dataFormatting('name', dictionary_object[key], pokemonName)
        #format_CLI(dictionary_object[key], list_keys)

    try:
        img = Image.open(BytesIO(data))
        # Display the image
        img.show()

    except Exception as e:
        print(f"Error: {e}")

    if saved_menu == True:
        return 5

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
        

    if display_input == 1:
        os.system('cls')
        return 2
    
    if display_input == 2:
        os.system('cls')
        return 1

    if display_input == 3:
        puts(colored.red('\n Pokemon has been saved'))
        savedPokemonList((0, pokemonName))
        time.sleep(2)
        return 10
       

    if display_input == 4:
        os.system('cls')
        return 10

    if display_input == 5:
        os.system('cls')
        return 6
    