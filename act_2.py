def reverse_bits(n):
    if n==0:
        return 0,"0"
    bl=n.bit_length()
    rev=0
    for i in range(bl):
        rev=(rev<<1) | ((n>>i)&1)
    return rev, format(rev,f'0{bl}b')


number=int(input("Enter your original number: "))

if number<0:
    print("Invalid input")
    exit()
rev, rev_bin=reverse_bits(number)
orig_bin=format(number,f'0{number.bit_length()}b') if number>0 else "0"
print(f"Enter your original number: {number} ({orig_bin})")
print(f"Reversed Number : {rev} ({rev_bin})")