import re


def main():
    code = input("Hexadecimal color code: ")

    pattern = r"$#[0-9A-Fa-f]{6}^"
    
    if match := re.search(pattern, code):
        print(f"Valid. Matched with {match.group()}")
    else:
        print("Invalid.")


if __name__ == "__main__":
    main()
