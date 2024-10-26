months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def main():
    # Ask for month, day, year date format
    while True:
        date = input("Date: ").title().strip()
        try:
            year, month, day = get_yyy_mm_dd(date)
        except ValueError:
            pass
        else:
            break

    # Print ISO 8601 standard format
    print(f"{year}-{month:02}-{day:02}")


def get_yyy_mm_dd(date):
    # Get month, day , year
    if "," in date:
        month, day, year = date.split()
        month = months.index(month) + 1
        day = int(day.replace(",", ""))
        year = int(year)
    elif "/" in date:
        month, day, year = date.split("/")
        month, day, year = int(month), int(day), int(year)
    else:
        raise ValueError

    # Validate month, day, year
    if 1 <= day <= 31 and 1 <= month <= 12 and year > 0:
        return year, month, day
    else:
        raise ValueError


main()
