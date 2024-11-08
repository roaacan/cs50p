import re


url = input("URL: ").strip()
if matches := re.search(r"^(?:https?://)?(?:www\.)?(?:twitter|x)\.com/([a-z0-9_]+)$", url, flags=re.IGNORECASE):
    print("Username:", matches.group(1))


#username = re.sub(r"(https?://)?(www\.)?(twitter|x)\.com/", "", url)

