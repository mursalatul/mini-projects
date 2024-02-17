from math import log2
from random import randint
from shutil import ExecError

def maximum_allowed_guess(n: int) -> int:
    return int(log2(n))

def welcome():
    welcome_text = "Welcome to Number Guessing Game"
    print(welcome_text.center(len(welcome_text) + 10, "*"))


def main():
    welcome()
    # status of the program
    statue = True # False when user enter false input
    # store total score
    score = 0
    while True:
        try:
            enter = int(input("Option (1. Play, 2. Exit) : "))
            if enter == 2:
                # exit section
                if score > 0:
                    print(f"Total Score: {score}")
                print("Game Ended")
                break
            elif enter == 1:
                # play section
                low, high = [int(i) for i in input("Enter low and high number(Example: 1 10): ").split()]
                maximum_allowed_guess_number = maximum_allowed_guess(high - low + 1)
                answer = randint(low, high)
                print("Maximum Guesses allowed:", maximum_allowed_guess_number)
                for i in range(maximum_allowed_guess_number):
                    guess = int(input("Guess: "))
                    if guess == answer:
                        score += maximum_allowed_guess_number - i
                        print("Correct guess!")
                        print("Score: ", maximum_allowed_guess_number - i)
                        print("Total Score: ", score)
                        break
                    else:
                        print("Wrong guess!", end="")
                        if guess > answer:
                            print(f"{guess} is greater then answer.")
                        else:
                            print(f"{guess} is less then answer")
                        print("Number of guesses left:", maximum_allowed_guess_number - i - 1)
            else:
                print("Wrong Input. Press 2 to exit or 1 to play")
        except ExecError as e:
            print("Wrong Input. Press 2 to exit or 1 to play")

if __name__ == "__main__":
    main()