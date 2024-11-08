import re

email = input("What's your email? ").strip()


if re.search(r"^(\w|\.)+@(\w+\.)+com$", email, flags=re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")