from DataValidation import dataValidation
import os
from clint.textui import colored, puts

def mainMenu():
    validation = False
    while not validation:

        print('Welcome to poke-Display! From the options below please enter the corresponding number and hit enter! \n')
        print('1. Display Random Pokemon (Recommended) ')
        print('2. Search By Pokemon Name or Type')
        print('3. Saved Pokemon List')
        print('4. Help')
        print('5. Update Notes')
        print('6. Exit')
        
        user_input = input('Enter the number here: ')
        
        result = dataValidation(1, 6, user_input) 
        validation = result[0]
        if validation == True:
            user_input = result[1]
                   
    if user_input == 1:
        return 1
    if user_input == 2:
        return 2
    if user_input == 3:
        return 5
    if user_input == 4:
        return 6
    if user_input == 5:
        return 7
    if user_input == 6:
        return 8

    return user_input