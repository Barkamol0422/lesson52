def power(a,b):
    result=1
    while(b>0):
        if (b%2==0):
            a=a*a
            b>>=1
        else:
            b=b-1
            result=result*a
    return result
a=int(input("Enter a number for x^y: "))
b=int(input("enter a number for x^y: "))
print(power(a,b))