def print_list(list, idx = 0):
    if(idx == len(list)):
        return
    print(list [idx])
    print_list(list, idx + 1)

cartoon = ["tom", "jerry", "richirich", "pinney", "pooh", "loonytoons", "Ben 10", "doremon"]

#print(print_list(cartoon))

print(list.reverse(cartoon))