def getAmountPrice():
    global _amount, _price
    _amount = int(input("Enter your amount of money: "))
    _price = int(input("Enter the price of apple: "))
    return int(_amount/_price)

def getChange():
    _change = enterAmountPrice*_price
    return int(_amount%_change)

def display(enterAmountPrice,changeComputation):
    print(f"You can buy {enterAmountPrice} apples and your change is {changeComputation} pesos.")

enterAmountPrice = getAmountPrice()
changeComputation = getChange()
display(enterAmountPrice,changeComputation)