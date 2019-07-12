x=int(input())
sums=0
temp=0
while(x>0):
    temp=x%10
    sums=sums+temp
    x=x//10
print(sums)
