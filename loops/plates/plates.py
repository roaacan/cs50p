def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 <= len(s) <= 6 and s[:2].isalpha() and s.isalnum():
        if not s.isalpha():
            # Validate numbers
            for i, c in enumerate(s):
                if c.isdigit():
                    return (s[i:].isdigit() and c != "0")
        return True
    else:
        return False


main()