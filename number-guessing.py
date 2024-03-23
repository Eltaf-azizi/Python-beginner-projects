import random 

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'guess the number between 1 and {x}: '))
        if guess > random_number:
            print('guess the number lower')
        elif guess < random_number:
            print('guess the number higher')
    print('Yah, the number you guessed is correct!')
    
guess(100)