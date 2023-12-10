import os 
from clint.textui import colored, puts

def helpMenu():
    os.system('cls')
    read_file = open("HelpMenu.txt", "r")
    for line in read_file:
        print(line)
    puts(colored.red('\n Enter any key to return to the main menu:'))
    input()
    return 10