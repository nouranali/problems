k,n,w=map(int,input().split())
c=k * (w*(w+1)//2) -n
print( c if c>0 else 0)
