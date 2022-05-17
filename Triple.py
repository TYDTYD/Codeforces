import sys
input=sys.stdin.readline

t=int(input())

for i in range(t):
    plag=False
    n=int(input())
    index=list(map(int,input().split()))
    m=max(index)
    array=[0]*(m+1)
    for j in index:
        array[j]+=1
        if array[j]>=3:
            print(j)
            plag=True
            break
    if plag==False:
        print(-1)
