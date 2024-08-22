grade = int(input("What is your grade?: "))

if grade >= 75 and grade <= 100:
    print('\nYou passed')

elif grade == 74:
    print('\nYou failed')
elif grade < 74 and grade > 0:
    print('\nYou will take remedial')
else:
    print('==========================================')
    print('Must input 0-100')
    print('Do not input negative numbers')
    print('==========================================')
