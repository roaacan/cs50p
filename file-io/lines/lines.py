import sys


def main():
    # Validate command-line arguments
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith("py"):
        sys.exit("Not a Python file")

    # Open python file
    try:
        file = open(sys.argv[1], "r")
    except FileNotFoundError:
        sys.close("File does not exist")

    # Count code lines
    print(count_code_lines(file))
    file.close()


def count_code_lines(file):
    code_lines = 0
    for line in file:
        if not line.isspace() and not line.lstrip().startswith("# "):
            code_lines += 1

    return code_lines


if __name__ == "__main__":
    main()
