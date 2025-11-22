def rightmost_set_bit(n):
    if n==0:
        return 0
    return (n&-n).bit_length()

num = int(input("Enter number: "))
if num<0:
    print("Invalid input")
    exit()

orig_bin=format(num, 'b') if num>0 else '0'
pos=rightmost_set_bit(num)
print(f"Enter number: {num} ({orig_bin})")
print(f"Position of the first set bit: {pos}")