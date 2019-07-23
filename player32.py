opens=['(']
close=[')']
def check(s):
    stack=[]
    for i in s:
        if i in opens:
            stack.append(i)
        elif i in close:
            pos=close.index(i)
            if((len(stack)>0) and (opens[pos]==stack[len(stack)-1])):
               stack.pop()
            else:
               return "Unbalanced"
        if len(stack)==0:
               return "Balance"
string=input()
print(check(string))
