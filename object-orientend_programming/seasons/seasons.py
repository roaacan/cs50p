import sys
import inflect
from datetime import date


def main():
    # Get valid birth date
    try:
        birth_date = str_to_date(input("Date of Birth: "))
    except ValueError:
        sys.exit("Invalid date")

    # Get minutes alive and print min to words
    minutes = minutes_alive(birth_date)
    print(minutes_to_words(minutes))


def minutes_alive(birth_date):
    return (date.today() - birth_date).days * 24 * 60


def minutes_to_words(min):
    p = inflect.engine()
    return f"{p.number_to_words(min, andword="").capitalize()} minutes"


def str_to_date(str_date):
    return date.fromisoformat(str_date)


if __name__ == "__main__":
    main()
