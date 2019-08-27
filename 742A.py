n= int (input())
exp =0
if n!=0:
    if n % 4 == 0:
        exp = 4
    elif n % 4 != 0:
        exp = n % 4
elif n==0:
    exp=0
print(pow(8,exp)%10)
