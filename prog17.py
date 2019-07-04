x=int(input())
temp=x
while temp>0:
    r=temp%10
    sum=0
    sum=sum+r**3
    temp=temp/10
if temp==sum:
    print("yes")
else:
    print("no")
