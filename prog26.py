number=int(input())
lists=list(map(int,input().split()))
lists.sort()
for i in range(number):
  print(lists[i],end=' ')

