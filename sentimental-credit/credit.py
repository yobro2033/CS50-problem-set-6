cardNumber = str(input("Number: "))
if len(cardNumber) < 15 or len(cardNumber) > 16:
    print("INVALID")
else:
    if len(cardNumber) == 15:
        startPoint = int(cardNumber[0])
        if startPoint == 3:
            print("AMEX")
        else:
            print("INVALID")
    elif len(cardNumber) == 16:
        startPoint = int(cardNumber[0])
        if startPoint == 4:
            print("VISA")
        elif startPoint == 5:
            print("MASTERCARD")
        else:
            print("INVALID")