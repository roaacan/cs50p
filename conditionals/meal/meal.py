def main():
    time = input("What time is it? ")
    time = time.strip().lower()

    time_float = convert(time)

    # Indicate meal time
    if 7 <= time_float <= 8:
        print("breakfast time")
    elif 12 <= time_float <= 13:
        print("lunch time")
    elif 18 <= time_float <= 19:
        print("dinner time")


def convert(time):
    if time.endswith(("a.m.", "p.m.")):
        # 12 hours format
        hour_min, pm_am = time.split(" ")
        hours, minutes = hour_min.split(":")
        hours, minutes = float(hours), float(minutes)

        # Convert to 24 hours format
        if hours == 12 and pm_am == "a.m.":
            hours = 0
        elif pm_am == "p.m." and hours != 12:
            hours += 12

        time_float = hours + (minutes / 60)
    else:
        # 24 hours format
        hours, minutes = time.split(":")
        time_float = float(hours) + (float(minutes) / 60)
    
    return time_float


if __name__ == "__main__":
    main()