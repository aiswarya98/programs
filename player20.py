s=int(input())
c=0
t=[]
n=['a','a','b','i','k','l']
for j in range (0,s):
    t.append(input())
for j in t:
    f=sorted(j)
    if(n==f):
        c=c+1
print(c)
        
