string=input()
count=0
for i in string:
    if(i.isalpha() or i.isdigit()):
      count=count+1
if count!=0:
    print("Yes")
else:
    print("No")
