from clint.textui import colored, puts

def programUpdates():
    read_file = open("UpdateNotes.txt", "r")
    for text in read_file:
        print(text)
    puts(colored.red('\n Press enter to return to main menu:'))
    input()
    return 10