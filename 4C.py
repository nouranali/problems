n=int(input())
users=dict()
for i in range(n):
    st=str(input())
    if st in users:
        print(st+str(users[st]))
        users[st]+=1
    else:
        print("OK")
        users[st]=1
            
