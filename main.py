ohelp = """
/help:      Prints a list of all possible commands
/define:    Allows user to input values to be used in calculations
/add:       adds all defined variables
"""

def commandchecker():
    x = input()
    
    if x == '':
        print('Blank Command Go ahead and type something!')
        commandchecker()
    
    if x == '/help':
        print(help)
        commandchecker()
    
    if x == '/define':
        definevar()
        commandchecker()

    else:
        print('Invalid Command please enter /help for a list of commands')
        commandchecker()

def definevar():
    xvalues = []
    yvalues = []
    a = input('How many point sets do you have?: ')
    a = int(a)
    x = a
    while x > 0:
        print('1')
        x = x-1



commandchecker()
