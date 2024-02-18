from math import log2
from random import randint


def maximum_allowed_guess(n: int) -> int:
    """calculate maximum number of guessed a user can used.
    here we calculated the maximum iteration for binary search,
    as user can always chose middle number.

    Args:
        n (int): high - low + 1 (range)

    Returns:
        int: maximum allowd guessed
    """
    return int(log2(n))


def welcome() -> None:
    """show welcome message.
    """
    welcome_text = "Welcome to Number Guessing Game"
    print(welcome_text.center(len(welcome_text) + 10, "*"))


def end() -> None:
    """show ending message.
    """
    end_text = "Game Ended"
    print(end_text.center(len(end_text) + 10, "*"))


def main():
    """main function
    """
    # show welcome message
    welcome()
    score = 0
    while True:
        try:
            enter = int(input("Option (1. Play, 2. Exit) : "))
            if enter == 2:
                # exit section
                if score > 0:
                    print(f"Total Score: {score}")
                # show end message
                end()
                break
            elif enter == 1:
                # play section
                low, high = map(
                    int, input("Enter low and high number(Example: 1 10): ").split()
                )
                maximum_allowed_guess_number = maximum_allowed_guess(high - low + 1)
                answer = randint(low, high)
                answer_found = False  # when answer is guessed it will be True
                print("Maximum Guesses allowed:", maximum_allowed_guess_number)
                for i in range(maximum_allowed_guess_number):
                    # taking the guess
                    guess = int(input("Guess: "))

                    # prediction matches with the answer
                    if guess == answer:
                        # increament the score
                        # less guess used = more score
                        score += maximum_allowed_guess_number - i
                        print("Correct guess!")
                        print("Score: ", maximum_allowed_guess_number - i)
                        print("Total Score: ", score)
                        answer_found = True
                        break

                    else:
                        # giving a hint
                        print("Wrong guess!", end="")
                        if guess > answer:
                            print(f"{guess} is greater then answer.")
                        else:
                            print(f"{guess} is less then answer")
                        print("Number of guesses left:", maximum_allowed_guess_number - i - 1)
                # show answer if cant guess the answer
                if not answer_found:
                    print("Correct answer:", answer)
            else:
                print("Wrong Input. Press 2 to exit or 1 to play")
        except Exception as e:
            print("Wrong Input. Press 2 to exit or 1 to play")
        except KeyboardInterrupt:
            print("\nGame is closed with keyboard interrupt.")
            break



if __name__ == "__main__":
    main()
    exit()