# first summ in recursion

def rsum(n):
    if(n == 0):
        return 0
    return rsum(n-1) + n

print(rsum(10))