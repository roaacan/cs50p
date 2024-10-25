def main():
    name = input("Name: ")
    print(hello(name))
    print(hello())


def hello(to="world"):
    return f"hello, {to}"


if __name__ == "__main__":
    main()