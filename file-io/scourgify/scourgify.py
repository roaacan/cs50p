import sys
import csv


def main():
    # Validate command-line arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith("csv") and not sys.argv[2].endswith("csv"):
        sys.exit("Not a CSV file")

    # Open CSV files
    try:
        before = open(sys.argv[1], "r")
    except FileNotFoundError:
        sys.exit("Could not read", sys.argv[1])

    # Separate first name and last name
    students = []
    for row in csv.DictReader(before):
        last, first = row["name"].split(", ")
        students.append({"first": first, "last": last, "house": row["house"]})

    before.close()

    # Create a new csv file and write students
    with open(sys.argv[2], "w") as after:
        writer = csv.DictWriter(after, fieldnames=["first", "last", "house"])
        writer.writeheader()
        writer.writerows(students)


if __name__ == "__main__":
    main()
