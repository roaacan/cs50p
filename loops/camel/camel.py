def main():
    camel_case = input("camelCase: ").strip()

    # Convert camel case to snake case
    snake_case = ""
    for c in camel_case:
        if c.isupper():
            snake_case += "_"
        snake_case += c.lower()

    print(snake_case)


main()