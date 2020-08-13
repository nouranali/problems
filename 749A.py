n= int(input())
cnt=0;ls=[]
if n%2==1:
  ls.append('3 ')
  n-=3
  cnt+=1
while (n>0):
  ls.append('2 ')
  n-=2   
  cnt+=1 
print(cnt)
print(' '.join(map(str, ls)))
