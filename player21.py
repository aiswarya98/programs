n=int(input())
b=[]
for i in range(2,n):
    if(n%i==0):
        b.append(i)
        n=n//i
a=sorted(b)
print(*a) 
    
