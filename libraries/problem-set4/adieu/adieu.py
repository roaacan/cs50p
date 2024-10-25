import inflect


def main():
    # Ask for names
    names = []
    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            print()
            break

    # Join names
    p = inflect.engine()
    plural_names = p.join(names)

    # Print adieu to each name
    print("Adieu, adieu, to", plural_names)


if __name__ == "__main__":
    main()
