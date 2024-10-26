def main():
    prompt = input("Input: ").strip()
    short_prompt = shorten(prompt)
    print("Output:", short_prompt)


def shorten(word):
    # Eliminate vowels
    for c in word:
        if c in "aeiouAEIOU":
            word = word.replace(c, "")
    return word.strip()


if __name__ == "__main__":
    main()