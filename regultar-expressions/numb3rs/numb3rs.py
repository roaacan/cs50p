import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    pattern = r"^(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})$"

    if match := re.search(pattern, ip):

        # Validate each n in the ip
        for n in match.group("ip").split("."):
            if int(n) > 255:
                return False
        return True

    return False


if __name__ == "__main__":
    main()
