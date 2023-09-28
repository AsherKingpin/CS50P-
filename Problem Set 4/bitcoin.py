import requests
import sys
if len(sys.argv) != 2:
    print("Put a commandline argument")
else:
    page = requests.get(" https://api.coindesk.com/v1/bpi/currentprice.json")
    try:
        float(sys.argv[1])
    except ValueError:
        print("Put a number in command line argument")
    
    data = page.json()
    price = data["bpi"]["USD"]["rate_float"]
    price = float(price)
    amount = float(price) * float(sys.argv[1])
    print(f"${amount:,.4f}")

