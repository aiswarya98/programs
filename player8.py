x123=list(input())
for i in range(0,len(x),2):
    c123=x[i]
    x123[i]=x123[i+1]
    x123[i+1]=c123
for i in x123:
    print(i,end="")
