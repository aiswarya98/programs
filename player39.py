def check_Power(N,k):
    if(N!=0) and (k!=0):
        for i in range (1,20):
            x = k**i
            if x == N :
                print("yes")
                break
            elif x> N:
                print("no")
                break
N,k=map(int,input().split())
check_Power(N,k)
