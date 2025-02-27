# WAP to check if a list contains a palindrome of elements. (Hint: use copy() m

list =[1, 2, 3, 4, 5]

list_copy = list.copy()
list_copy.reverse()

if(list == list_copy):
    print("This Is a Palindrome")
else:
    print("this is not Palindrom")
