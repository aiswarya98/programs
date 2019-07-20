x,y=map(int,input().split())
num=1
while(num>0):
    if((num%x)==0 and (num%y)==0):
            print(num)
            num=0
    else:
            num+=1
