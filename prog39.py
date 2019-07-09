x1,y1=map(int,input().split())
temp=0
if(x>y) or (x<y):
    temp=x1
    x1=y1
    y1=temp
print(x1,y1)
