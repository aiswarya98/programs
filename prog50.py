import statistics
x=int(input())
for i in range(x):
    y=list(map(int,input().split()))
    print(statistics.mean(y))
