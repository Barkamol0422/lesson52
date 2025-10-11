def a(n):
    c=0
    while (n):
        c+=1
        n>>=1
    return c
n=int(input("Enter a number: "))
print("Bits in the number: ",a(n))
