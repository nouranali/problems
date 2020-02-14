n=int(input())
cnt=0
for i in range(n):
    st=input()
    if st== "++X" or st=="X++":
        cnt+=1
    else:
        cnt-=1

print(cnt)    
