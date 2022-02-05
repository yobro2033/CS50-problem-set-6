cardNumber = str(input("Number: "))
if len(cardNumber) < 15 or len(cardNumber) > 16:
    print("INVALID")
else:
    if len(cardNumber) == 15:
        if cardNumber[0] == 3:
            print("AMEX")
        else:
            print("INVALID")
    elif len(cardNumber) == 16:
        if cardNumber[0] == 4:
            print("VISA")
        elif cardNumber[0] == 5:
            print("MASTERCARD")
        else:
            print("INVALID")
