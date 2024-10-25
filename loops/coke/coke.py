def main():
    coke_price = 50
    amount_due = coke_price
    count_cents = 0

    while count_cents < coke_price:
        print("Amount Due:", amount_due)
        cents = input("Insert Coin: ")

        # Validate and count coins
        if cents == "25" or cents == "10" or cents == "5":
           count_cents += int(cents)
           amount_due -= int(cents)
        
    # Calculate changed
    print("Change Owed:", count_cents - coke_price)


main()
