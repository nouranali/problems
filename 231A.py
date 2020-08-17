res=0
for _ in range(int(input())):
  l=list(map(int,input().split()))
  if sum(l)>1:
    res+=1
print(res)
