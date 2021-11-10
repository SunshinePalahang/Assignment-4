def getNameAgeAdd():
    _name = input("Enter name: ")
    _age = input("Enter age: ")
    _add = input("Enter address: ") 
    return _name,_age,_add

def display(name, age, add):
    print(f"Hi, my name is {name}. I am {age} years old and I live in {add}.")

name, age, add = getNameAgeAdd()
display(name, age, add)