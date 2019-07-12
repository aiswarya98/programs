powernumber=int(input())
b=powernumber & powernumber-1
if(b==0):
    print("yes")
else:
    print("no")
