import random 
import string
   
pass_len = int(input("Enter Passwd Length : "))
charValues = string.ascii_letters + string.digits + string.punctuation

password = "".join([random.choice(charValues) for i in range(pass_len)])


"""""
for i in range(pass_len):
    password += random.choice(charValues)
"""
print("your random password is", password)


