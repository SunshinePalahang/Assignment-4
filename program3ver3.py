def getAmountPrice():
    global _amount, _price
    _amount = int(input("Enter your amount of money: "))
    _price = int(input("Enter the price of apple: "))
    return int(_amount/_price)

def 

#Create a program which you will enter the amount of money you have, it will also ask for the price of an apple.
enterAmountPrice = getAmountPrice()
#Display the maximum number of apples that you can buy and the remaining money that you will have.
changeComputation = getChange()
#Display the output in the following format.
#You can buy ___ apples and your change is ___ pesos.
