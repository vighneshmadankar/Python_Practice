#recursive FUNCTION

def show(n):
    if(n == 0): # BASE CASE
        return
    print(n)
    show(n-1)
show(100)