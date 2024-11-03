import sys
import csv


def main():
    # Validate command-line arguments
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith("csv"):
        sys.exit("Not a CSV file")

    # Open csv file
    try:
        csv_file = open(sys.argv[1], "r")
    except FileNotFoundError:
        sys.exit("File does not exit")

    create_table(csv_file)
    csv_file.close()


def create_table(csv_file):
    ...


if __name__ == "__main__":
    main()