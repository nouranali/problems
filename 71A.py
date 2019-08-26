import functools
n= int(input())
ls= list()
for i in range(n):
    word = str(input())
    if len(word)>10:
        ls.append(word[0] + str(len(word) - 2) + word[len(word)-1])
    elif len(word)<= 10:
        ls.append(word)
for i in range (n):
    print(ls[i])