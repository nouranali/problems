n,m,k=map(int,input().split())
flag=True if k%2==0 else False
for i in range(1,n+1):
  if k<= i*m*2:
    print(i , ((k - 1) // 2) % m + 1 ,'R' if flag else 'L')
    break
