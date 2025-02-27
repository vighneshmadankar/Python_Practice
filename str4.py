# Wap to find gretest of three nummber
num1 = int(input("Enter NUM1: "))
num2 = int(input("Enter NUM2: "))
num3 = int(input("Enter NUM3: "))

if(num1 > num2 and num1 > num3):
    print("Num1 Is Greatest")
elif(num2 > num1 and num2 > num3):
    print("Num2 Is Greatest")
elif(num3 > num1 and num3 > num2):
    print("Num3 Is Greatest")