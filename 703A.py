res=0
for i in range(int(input())):
  m,c=map(int,input().split())
  res+= m>c; res-=c>m
print('Mishka' if res>0 else ['Friendship is magic!^^','Chris'][res<0])
