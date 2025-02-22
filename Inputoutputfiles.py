with open("Practice.txt","r") as f:
    data = f.read()
new_data = data.replace("java", "Python")
print(new_data)

with open("Practice.txt","w") as f:
    f.write(new_data)
    

