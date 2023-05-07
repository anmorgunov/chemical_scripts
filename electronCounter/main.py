import countElectrons

def electron_counter_wrapper():
    print('Please type Q to return to main menu')
    while True:
        formula = input('Please enter chemical formula: ')
        if formula == 'Q':
            break
        # print(f"Your molecule has {countElectrons.count_electrons(formula)} electrons\n")
        print(countElectrons.count_electrons(formula))

while True:
    menu = '''
------- What would you like to do? ---------
1. Count number of electrons
11. Exit
'''
    print(menu)
    selector = int(input('Choose menu item: '))
    if selector == 11:
        break
    codeToFun = {
        1: electron_counter_wrapper
    }
    codeToFun[selector]()

