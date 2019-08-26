n,total = map(int,input().split())
no =0
for i in range(n) :
    char,d= input().split()
    d=int(d)
    if char=='+':
        total+=d
    else:
        if total<d:
            no+=1
        elif total >= d:
            total-=d
print(total,no)
