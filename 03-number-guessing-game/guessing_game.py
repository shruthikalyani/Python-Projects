import random
print('='*40)
print('     NUMBER GUESSING GAME')
print('      by Shruthi Kalyani')
print('='*40)
print('\n')
while True:
    number=random.randint(1,100)
    attempts=0
    print('\n Im thinking of a number between 1 and 100!')
    print('try to guess it!!!')
    while True:
        try:
            guess=int(input('enter your guess:'))
            attempts+=1
            if guess<1 or guess>100:
                print('please enter a number between 1 and 100')
                continue
            elif guess>number:
                print('lower ^u^')
            elif guess<number:
                print('higher ;)')
            else:
                print(f'correct! you got it in {attempts} attempts!')
                if attempts<=5:
                    print('Excellent!!!')
                elif attempts<=10:
                    print('Good Job!')
                else:
                    print('you can do better next time!')
                break
        except ValueError:
            print('please enter a valid WHOLE number')
    choice=input('do you want to play again? (y/n):')
    if choice.lower()!='y':
        print('Thanks for playing! Goodbye!')
        break