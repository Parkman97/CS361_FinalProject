import os
from clint.textui import colored, puts

def dataValidation(lower, upper, value):
    try:
        value = int(value)

        if value <= upper and value >= lower:
            return (True, value)
        else:
            os.system('cls')
            puts(colored.red('Invalid input. Please enter a valid number.\n')) 
            return (False, value)
    except ValueError:
            os.system('cls')
            puts(colored.red('Invalid input. Please enter a valid number.\n')) 
            return (False, value)      