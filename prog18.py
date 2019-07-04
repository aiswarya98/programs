x,y=map(int,input().split())
for i in range(x+1,y):
    temp=i
    while i>0:
       r=temp%10
       sum=0
       sum=sum+r**3
       temp=temp/10
    if i==sum:
       print(i,end=' ')
