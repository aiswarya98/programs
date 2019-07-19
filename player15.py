x=int(input())
s=str(input())
l=('A','E','I','0','U','a','e','i','o','u')
for i in s:
    if i in l:
        s=s.replace(i,"")
print(s[::-1])
