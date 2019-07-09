x,y=map(int,input().split())
temp=0
if(x>y) or (x<y):
    temp=x
    x=y
    y=temp
print(x,y)
