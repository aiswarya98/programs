m,n=list(map(int,input().split()))
l=list(map(int,input().split()[:m]))
for i in range(0,n):
   l=([l[-1]] + l[:-1])
print(*l)
