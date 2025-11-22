def power8(number):
    if number<=0:
        return False
    if number&(number-1):
        return False
    count=0
    while number>1:
        number>>=1
        count+=1
    return (count%3)==0

number=int(input("Enter a number: "))
if power8(number):
    print(number,"is power of 8")
else:
    print(number,"is not power of 8")