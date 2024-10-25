import random


def main():
    # Ask level
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            pass
        else:
            if level > 0:
                break

    # Generate number between 1 and n
    number = random.randint(1, level)

    # Guess number
    guess = 0
    while guess != number:

        # Catch excepctions
        try:
            guess = int(input("Guess: "))
        except ValueError:
            pass
        else:
            if guess > 0:
                if number > guess:
                    print("Too small!")
                elif number < guess:
                    print("Too large!")
                else:
                    print("Just right!")


if __name__ == "__main__":
    main()
