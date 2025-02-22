# GUSSING GAME ~~TRY YOUR LUCK~~ 
import random

randnum = random.randint(1, 99)

while True:
    nval = input("Enter A Lucky Lottry Num Here  Or Enter (Q) to Exit Game@@:~")
    if(nval == "Q"):
        print("~~~~~~~~~GAME OVER~~~~~~~~")
        break

    nval = int(nval)

    if(nval == randnum):
        print("Congrats!!!, You Won the Lottry")
        break

    elif(nval < randnum):
        print("Your num is Greter than result :")

    elif(nval > randnum):
        print("Your num is Lesser than result :")

    else:
        print("Better Luck Next Time !!")

print("Your Random Num is ",randnum)
