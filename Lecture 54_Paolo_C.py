def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "1234" and passwordInput == "1234":
        return showMenu()
    else:
        return login()

def showMenu():
    print("----- PShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    return menuSelect()

def menuSelect():
    userSelected = int(input(">> "))
    if userSelected == 1:
        return vatCalculator()
    elif userSelected == 2:
        return  priceCalculator()
    else:
        print(" กรุณาเลือก 1 หรือ 2")
        showMenu()

def vatCalculator():
    vat = 7
    UserInputVat = int(input("ราคาสินค้า : "))
    result = UserInputVat + (UserInputVat * vat / 100)
    print(result)

def priceCalculator():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    print(price1 + price2)

login()