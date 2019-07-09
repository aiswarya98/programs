x=str(input())
count=0
for i in range(0,len(x)):
    if(x[i]!=' ' and x[i+1]==' '):
        count=count+1;
print(count)
