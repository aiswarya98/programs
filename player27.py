x=input()
l=[]
for i in x:
    if(i.islower()):
        l.append(i.upper())
    else:
        l.append(i.lower())
for i in l:
    print(i,end=' ')
