import math
x,y=map(int,input().split())
count=0
for i in range(x,y+1):
    if(math.sqrt(i)*math.sqrt(i)==i):
        count+=1
print(count)
