x=(int(input()))
temp=x
sos=0
while(x!=0):
    temp=x%10
    sos+=temp*temp
    x=x//10
print(sos)
