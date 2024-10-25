import random


cards = ["king", "queen", "jack"]


def main():
    random.seed(102)
    card = random.choice(cards)
    print(card)

    # Plural
    print(random.choices(cards, k=2))
    print(random.sample(cards, k=2))
    print(random.choices(cards, weights=[80, 19, 1], k=2))


main()
