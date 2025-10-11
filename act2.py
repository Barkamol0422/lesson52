def isodd(n):
    if (n^1==n+1):
        return True
    else:
        return False
n=int(input("Please enter a number to check it is odd or even: "))
if isodd(n):
    print(n,"is even number.")
else:
    print(n,"is odd number")
