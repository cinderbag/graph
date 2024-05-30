from num2words import num2words

help = """
/help:      Prints a list of all possible commands
/define:    Allows user to input values to be used in calculations 
"""

def commandchecker():
    x = input()
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
        n = 1
        xval = input('What is the' +  + ' x value?')
        yval = input('What is the' +  + ' y value?')

print('Welcome to graph utility type /help for a list of commands')

commandchecker()