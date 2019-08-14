n=int(input())
s=list(map(int,input().split()[:n]))
if(s==sorted(s)):  
    print ("yes") 
else: 
    print ("no") 
