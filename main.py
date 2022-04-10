import random

mani = 100

while True:
    while True:
        ff = input("Play(+, -): ")
        if ff == "-":
            break
        elif ff == "+":
            break
        else:
            print("ERROR")
    if ff == "-":
        break
    while True:
        uu = int(input("Stavka: "))
        if uu > mani:
            print("ERROR")
        elif uu <= 0:
            print("ERROR")
        else:
            break
    while True:
        ii = int(input("Na kakoe(1, 10): "))
        if ii <= 0:
            print("ERROR")
        elif ii > 10:
            print("ERROR")
        else:
            break
    yy = random.randint(1, 10)
    if ii == yy:
        mani = mani + uu
        print("Win")
        print("Mani: " + str(mani))
    else:
        mani = mani - uu
        print("Luser")
        print("Winer: " + str(yy))
        print("Mani: " + str(mani))
    if mani <= 0:
        print("No mani")
        break