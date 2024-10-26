def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
        except (ValueError, ZeroDivisionError):
            continue
        else:
            break
    
    print(gauge(percentage))


def convert(fraction):
    x, y = fraction.split("/")
    if int(y) == 0:
        raise ZeroDivisionError
    elif int(x) > int(y):
        raise ValueError("x is greater than y")

    return round((int(x) / int(y)) * 100)


def gauge(percentage):
    if 0 <= percentage <= 1:
        return "E"
    elif 99 <= percentage <= 100:
        return "F"
    else:
        return  f"{round(percentage)}%"


if __name__ == "__main__":
    main()
