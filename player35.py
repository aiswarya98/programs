n,k=map(int,input().split())
res = [int(i) for i in str(n)] 
for i in res:
    count=0
    if(i==k):
        count+=1
print(count)
