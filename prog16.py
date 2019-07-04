x,y=map(int,input().split())
for i in range(x,y):
    if i>1:
        for n in range(2,i):
            if(i%n)==0:
                break
            else:
                print(set(i), end=' ')
