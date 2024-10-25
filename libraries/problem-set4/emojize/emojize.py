import emoji


def main():
    s = input("Input: ")
    emojized = emoji.emojize(s, language="alias")
    print("Output:", emojized)


if __name__ == "__main__":
    main()
