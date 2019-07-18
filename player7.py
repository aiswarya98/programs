m,p=map(str,input().split())
for i in range(len(m)):
    if(m.count(m[i])==p.count(p[i])):
        print("yes")
        break
    else:
        print("no")
        break
        
