def main():
    yell("hello, world", "this is cs50")


def yell(*phrases):
    # uppercased = map(str.upper, phrases)
    uppercased = [phrase.upper() for phrase in phrases]
    print(*uppercased, sep=" - ")


if __name__ == "__main__":
    main()