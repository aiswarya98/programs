def minMultipleK( n, k): 
    min = (n // 2) + (n % 2) 
    for i in range(min, n + 1): 
        if (i % k == 0): 
            return i        
    return -1
n,k=map(int,input().split())
print(minMultipleK( n, k))
