def main():
    prompt = input("What is the answer to the Great Question of Life, the Universe and Everything? ")
    prompt = prompt.strip().lower()
    match prompt:
        case "42" | "forty-two" | "forty two":
            print("Yes")
        case _:
            print("No")


main()