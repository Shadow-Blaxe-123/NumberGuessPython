import random

guess: int = random.randint(0,101)
gameOver: bool = False


if __name__ == '__main__':
    while not gameOver:
        user_input = input('Guess the number: ')
        if user_input:
            gameOver = True

