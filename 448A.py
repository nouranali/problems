a= list(map(int,input().split()))
b=  list(map(int,input().split()))
n= int(input())
if (sum(a)+4)//5 + (sum(b)+9)//10 <=n:
  print('YES')
else: 
  print('NO')  
