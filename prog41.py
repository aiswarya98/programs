n=int(input())
d=0
b=1
count=0
while(count<n):
    print(d,end=' ')
    s=d+b
    d=b
    b=s
    count=count+1
