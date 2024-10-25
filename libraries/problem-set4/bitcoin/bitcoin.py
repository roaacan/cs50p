import sys
import requests


def main():
    # Check command-line arguments
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")

    # Convert argument to float
    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    # Connect API and Request CoinDesk Bitcoin Price
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except requests.RequestException:
        sys.exit()

    # Get bitcoin price in USD
    o = response.json()
    usd_price = o["bpi"]["USD"]["rate_float"]

    # Covert bitcoin in USD
    bitcoin_price = usd_price * n
    print(f"${bitcoin_price:,}")


if __name__ == "__main__":
    main()
