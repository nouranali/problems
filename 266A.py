n=int(input())
st=str(input())
cnt=0
for i in range(n-1):
    if st[i+1]==st[i]:
        cnt+=1
print(cnt)        
