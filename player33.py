x,y=map(int,input().split())
list123=list(map(int,input().split()[:x]))
if y in list123:
    print("yes")
else:
    print("no")
