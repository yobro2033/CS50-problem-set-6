Qcoins = 0
Dcoins = 0
Ncoins = 0
Pcoins = 0
total = 0

def numberQ():
    global Qcoins
    global changeToPay
    Qcoins = changeToPay // 0.25
    if Qcoins != 0:
        changeToPay = changeToPay - (Qcoins*0.25)
        changeToPay = round(changeToPay,2)
        Qcoins = Qcoins
    else:
        changeToPay = changeToPay
        Qcoins = 0
    return Qcoins, changeToPay

def numberD():
    global Dcoins
    global changeToPay
    Dcoins = changeToPay // 0.1
    if Dcoins != 0:
        changeToPay = changeToPay - (Dcoins*0.1)
        changeToPay = round(changeToPay,2)
        Dcoins = Dcoins
    else:
        changeToPay = changeToPay
        Dcoins = 0
    return Dcoins, changeToPay

def numberN():
    global Ncoins
    global changeToPay
    Ncoins = changeToPay // 0.05
    if Ncoins != 0:
        changeToPay = changeToPay - (Ncoins*0.05)
        changeToPay = round(changeToPay,2)
        Ncoins = Ncoins
    else:
        changeToPay = changeToPay
        Ncoins = 0
    return Ncoins, changeToPay

def numberP():
    global Pcoins
    global changeToPay
    Pcoins = changeToPay // 0.01
    if Pcoins != 0:
        changeToPay = changeToPay - (Pcoins*0.01)
        changeToPay = round(changeToPay,2)
        Pcoins = Pcoins
    else:
        changeToPay = changeToPay
        Pcoins = 0
    return Pcoins, changeToPay

while True:
    try:
        changeToPay = float(input("Change owed: "))
        if changeToPay < 0:
            raise ValueError
        else:
            break
    except ValueError:
        print("Invalid input")

quarters = numberQ()
dimes = numberD()
nickels = numberN()
pennies = numberP()
total = int(Qcoins + Dcoins + Ncoins + Pcoins)
print(total)