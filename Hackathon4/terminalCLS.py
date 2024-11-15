import os
def cls():
    '''
    This function clears the terminal
    '''
    os.system('cls' if os.name=='nt' else 'clear')
# Uses the function "cls" for clearing the console
cls()