number=int(input())
slists=list(map(int,input().split()))
for i in slists:
    if slists.count(i)==1:
        b=slists.count(i)
        c=i
print(c)
