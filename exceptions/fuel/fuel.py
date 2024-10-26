def main():
    # Ask for a fuel fraction
    while True:
        fraction = input("Fraction: ")
        
        try:
            x, y = fraction.split("/")
            div = int(x) / int(y)
        except (ValueError, ZeroDivisionError):
            pass
        else:
            if 0 <= div <= 1:
                break

    # Show fuel remains
    percentage = div * 100
    if 0 <= percentage <= 1:
        print("E")
    elif 99 <= percentage <= 100:
        print("F")
    else:
        print(f"{round(percentage)}%")


main()
