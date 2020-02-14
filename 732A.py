k,r = map(int,input().split())
i=1
while i>0:
     if (i*k)%10 ==0 or (i*k -r) %10 ==0:
         print(i)
         break
     i+=1