n= int(input())
ls = [int(x) for x in input().split()]
cntls=[]
def subseg ():
    cnt=1
    if (n!=1):
        for i in range(len(ls) - 1):
            if (ls[i + 1] >= ls[i]):
                cnt = cnt + 1
                cntls.append(cnt)
            else:
                cnt = 1
                cntls.append(cnt)
    else:
        cntls.append(1)
        cntls.append(0)
    return max(cntls)
res = subseg()
print(res)
