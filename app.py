import random


def game():
    random_Num = random.randint(0, 100)
    'to test uncomment'
    'print(random_Num)'
    user_Guess = int(input('guess a number from 0 to 100: '))

    def compare(num, guess):
        if guess == num:
            print('you guessed the correct number!')
            user_response = input('would you like to play again (y/n)? ')
            if user_response.lower() == 'y':
                game()
            elif user_response.lower() == 'n':
                print('Good Game. Thank you for playing!')
        elif guess != num:
            print('you guessed incorrectly')
            user_response = int(input('please guess again: '))
            compare(random_Num, user_response)

    compare(random_Num, user_Guess)


game()
