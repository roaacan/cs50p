from random import randint


def main():
    # Ask for level
    level = get_level()

    # Generate addition problems
    score = 0
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)

        attemps = 3

        # Show additionl problem and ask for solution
        while attemps > 0:
            solution = int(input(f"{x} + {y} = "))

            # Check solution
            if solution == (x + y):
                score = score + 1
                break
            else:
                print("EEE")
                attemps = attemps - 1

        # Show solution if user doesn't answer correctly
        if attemps == 0:
            print(f"{x} + {y} = {x + y}")

    # Show score
    print("Score:", score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            pass
        else:
            if 0 < level < 4:
                return level


def generate_integer(level):
    if level == 1:
        return randint(0, 9)
    elif level == 2:
        return randint(10, 99)
    elif level == 3:
        return randint(100, 999)


if __name__ == "__main__":
    main()
