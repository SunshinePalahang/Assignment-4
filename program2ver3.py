def getAppleOrangeQty():
    _appleQty = int(input("How many apple? "))
    _orangeQty =int(input("How many orange? "))
    return int(_appleQty*(20) + _orangeQty*(25))

def display(AppleOrangeQty):
    print (f"The total amount is {AppleOrangeQty}.")

AppleOrangeQty = getAppleOrangeQty()

display(AppleOrangeQty)