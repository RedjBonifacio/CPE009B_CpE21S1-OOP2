grade = int(input("What is your grade?: "))

if grade >= 75:
    print('You passed')
elif grade == 74:
    print('You will take remedial')
elif grade < 74:
    print('You failed')