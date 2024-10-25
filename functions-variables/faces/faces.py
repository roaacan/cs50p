def main():
    prompt = input().strip()
    output = prompt.replace(":)", "🙂")
    output = output.replace(":(", "🙁")
    print(output)


main()