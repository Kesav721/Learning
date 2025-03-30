import random

def guess(x):
    random_num=random.randint(1,x)
    guess=0
    while guess != random_num:
        guess=int(input(f'Guess a number between 1 and{x} :'))
        if guess < random_num:
            print('Sorry,guess again .Too Low')
        elif guess > random_num:
            print('Sorry,guess again .Too High')
        
    print (f'yay,congrats,you have guessed the number {random_num}correctly')
guess(10)
