import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern_find_url = r'src="(https?://(?:www\.)?youtube\.com/embed/\w+)"'
    pattern_replace_url = r"https?://(?:www\.)?youtube\.com/embed"

    if match := re.search(pattern_find_url, s, flags=re.IGNORECASE):
        youtube_url = match.group(1)
        return re.sub(pattern_replace_url, "https://youtu.be", youtube_url)

    return None


if __name__ == "__main__":
    main()
