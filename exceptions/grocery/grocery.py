def main():
    items = {}

    # Ask for items
    while True:
        try:
            item = input().upper().strip()
        except EOFError:
            break
        else:
            # Counts equal itmes
            if item in items:
                items[item] += 1
            else:
                items[item] = 1

    print()
    # Sort and print items
    for item in sorted(items):
        print(f"{items[item]} {item}")


main()
