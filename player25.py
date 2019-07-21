b=int(input(""))
x=list(map(str,input().split()[:b]))
x.sort()
x.sort(key=len)
for i in x:
       print(i,end=" ")
