import sys
import random
from pyfiglet import Figlet


figlet = Figlet()
fonts = figlet.getFonts()


def main():
    # Validate command-line arguments
    if len(sys.argv) == 1:
        font = random.choice(fonts)
    elif len(sys.argv) == 3:
        if sys.argv[1] in ["-f", "--font"] and sys.argv[2] in fonts:
            font = sys.argv[2]
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")

    # Set font
    figlet.setFont(font=font)

    # Ask for an input
    prompt = input("Input: ")

    # Print faglet format
    print(figlet.renderText(prompt))


if __name__ == "__main__":
    main()
