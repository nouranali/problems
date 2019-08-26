n = int(input())
ls = list(map(int,input().split()))
print(max(0,n-ls.count(max(ls))-ls.count(min(ls))))