def main():
    ...


def convert(au):
    if not isinstance(au, (int, float)):
        raise TypeError("au must be an int or a float")
    return au * 149597870700