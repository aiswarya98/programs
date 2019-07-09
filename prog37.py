sen=input()
count=0
for i in range(0,len(sen)):
    if(sen[i].isdigit() or sen[i].isalpha() or sen[i]==' '):
        continue
    else:
        count=count+1
print(count)

