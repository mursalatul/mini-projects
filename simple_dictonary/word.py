import random

words = ["apple", "banana", "car", "house", "cat", "dog", "book", "table", "chair", "phone", "computer", "person", "friend", "family", "city", "country", "school", "food", "water", "money", "time", "job", "bed", "door", "window", "tree", "flower", "road", "street", "building", "bird", "fish", "horse", "cow", "chicken", "airplane", "boat", "train", "bus", "bicycle", "camera", "guitar", "piano", "music", "movie", "television", "radio", "newspaper", "magazine", "internet", "website", "game", "toy", "child", "parent", "sibling", "aunt", "uncle", "cousin", "grandmother", "grandfather", "doctor", "nurse", "teacher", "student", "engineer", "scientist", "artist", "writer", "chef", "waiter", "waitress", "police", "firefighter", "soldier", "lawyer", "judge", "politician", "president", "king", "queen", "prince", "princess", "superhero", "villain", "monster", "robot", "alien", "ghost", "vampire", "werewolf", "zombie"]



def main() -> None:
    word = random.choice(words)
    score = 0
    while True:
        try:
            opt = int(input("Option (1. Play, 2. Exit)"))
            if opt == 2:
                if score > 0:
                    print("Score:", score)
                print("Game End")
                exit()
            elif opt == 1:
                life = len(word) - 1
                print("Guess the word")
                print("Word size:", len(word))
                status = False
                while life:
                    print("Life:", life)
                    print(f"Hint {len(word) - life}: {word[:len(word) - life]}")
                    guess = input("Word: ")
                    if guess == word:
                        score += life
                        print("Correct Guess", f"You have won {life} point", f"Total Score: {score}", sep='\n')
                        status = True
                        break
                    else:
                        print("Wrong Guess")
                        life -= 1
                if not status:
                    print("Round ended. the word was:", word)
        except Exception as e:
            print("Wrong Input.")

if __name__ == "__main__":
    main()