a,b,c=map(str,input().split())
c=int(c)
d=len(a)
count=0
for i in range(0,d):
    if(a[i]!=b[i]):
        count+=1
if(count==c):
    print("yes")
else:
    print("no")
        
