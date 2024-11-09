import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"^(?P<sh>\d+):?(?P<sm>\d+)? (?P<sp>AM|PM) to (?P<eh>\d+):?(?P<em>\d+)? (?P<ep>AM|PM)$"

    # Validate, input, hours and minutes
    if match := re.search(pattern, s):
        sh, sm, sp, eh, em, ep = match.groups()
        sh, eh = int(sh), int(eh)
        sm = int(sm) if sm else 0
        em = int(em) if em else 0

        # Validate range hours and minutes
        if not (0 < sh <= 12) or not (0 < eh <= 12):
            raise ValueError
        elif not (0 <= sm < 60) or not (0 <= em < 60):
            raise ValueError

        # Converting twelve to twenty-four
        start_hour, start_minute = twelve_to_twentyfour(sh, sm, sp)
        end_hour, end_minute = twelve_to_twentyfour(eh, em, ep)

        return f"{start_hour:02}:{start_minute:02} to {end_hour:02}:{end_minute:02}"

    else:
        raise ValueError


def twelve_to_twentyfour(hours, minutes, period):
    if hours == 12:
        hours = 0 if period == "AM" else 12
    elif period == "PM":
        hours = hours + 12

    return hours, minutes


if __name__ == "__main__":
    main()
