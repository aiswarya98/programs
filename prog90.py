string123=list(input())
string345=[]
for i in string123:
        if i not in string345:
        string345.append(i)
if(string123==string345):
    print("Yes")
else:
    print("No")
