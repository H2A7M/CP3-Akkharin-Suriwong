username = input("Usename : ")
passwod = input("Passwod : ")
Shirt = 290
T_shirt = 150
Long = 250
if username == "akkharin" and passwod == "1234":
    print("----Hamster Shop----")
    print("Clothing items")
    print("1.Shirt 290 THB")
    print("2.T-shirt 150 THB")
    print("3.Long sleeve shirt 250 THB")
    product = int(input("Please select a product (Number): "))
    amount = int(input("amount : "))
    print("--------------------")
    if product == 1:
        print("Receipt Hamster Shop")
        print("Shirt 290 THB *",amount,"=",Shirt*amount,"THB")
        print("--------------------")
        print("Thank you")
    elif product == 2:
        print("Receipt Hamster Shop")
        print("T-shirt 150 THB *", amount, "=", T_shirt * amount, "THB")
        print("--------------------")
        print("Thank you")
    elif product == 3:
        print("Receipt Hamster Shop")
        print("TLong sleeve shirt 250 THB *", amount, "=", Long * amount, "THB")
        print("--------------------")
        print("Thank you")
else:
    print("Plase check Username or Password !!!")