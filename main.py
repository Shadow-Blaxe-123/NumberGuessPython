import random

guess: int = random.randint(0, 101)
gameOver: bool = False


if __name__ == "__main__":
    while not gameOver:
        user_input = int(input("Guess the number: "))
        if user_input == guess:
            print("You won!")
            gameOver = True
        elif user_input < guess:
            print("Too low")
        elif user_input > guess:
            print("Too high")
