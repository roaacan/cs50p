def main():
    prompt = input("Input: ").strip()
    
    # Eliminate vowels
    for c in prompt:
        if c in "aeiouAEIOU":
            prompt = prompt.replace(c, "")

    print("Output:", prompt)
    
    
main()