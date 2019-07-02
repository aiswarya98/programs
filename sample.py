a=float(input("Enter a:"))
b=float(input("Enter b:"))
c=float(input("Enter c:"))
if(a==b==c):
    print("All the given numbers are equal")
elif((a<b)and(b>c)):
    print("b is greater")
elif((a>b)and(b<c)):
    print("a is greater")
else:
    print("c is greater")

