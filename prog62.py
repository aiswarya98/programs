x,y=map(int,input().split())
count=0
x1=list(map(int,input().split()))
for i in x1:
    if(i==y):
      count=count+1
print(count)
