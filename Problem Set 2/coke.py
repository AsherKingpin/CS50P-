Amount = 50  
while Amount > 0:
    coin = int(input("Insert Coin:"))
    if coin in (5,10,25):
        Amount = Amount - coin
    if Amount > 0:
        print("Amount Due:",Amount)
    else:
        print("Change owed:",-Amount)
    
