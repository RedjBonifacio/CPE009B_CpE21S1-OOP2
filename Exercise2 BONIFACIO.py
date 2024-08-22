grade = int(input("\nWhat is your grade?: "))

if grade >= 75 and grade <= 100:
    print('\nYou passed')

elif grade == 74:
    print('\nYou failed')
elif grade < 74 and grade > 0:
    print('\nYou need take remedial')
else:
    print('\n==========================================')
    print('(Inputted grade must only be 0 to 100)')
    print('==========================================')
