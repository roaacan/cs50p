import sys
from PIL import Image
from PIL import ImageOps


def main():
    # validate command-line arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[2].endswith(("jpg", "jpeg", "png")):
        sys.exit("Invalid output")
    elif not same_ext(sys.argv[1], sys.argv[2]):
        sys.exit("Input and output have different extensions")

    # Open images
    try:
        before = Image.open(sys.argv[1])
        shirt = Image.open("shirt.png")
    except FileNotFoundError:
        sys.exit("Input does not exit")

    # Resize and crop
    output = ImageOps.fit(before, shirt.size)

    # Paste image and save
    output.paste(shirt, mask=shirt)
    output.save(sys.argv[2])


def same_ext(file1, file2):
    return file1.split(".")[-1] == file2.split(".")[-1]


if __name__ == "__main__":
    main()
