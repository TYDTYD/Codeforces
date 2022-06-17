import sys
input=sys.stdin.readline

T=int(input())

for i in range(T):
    a=int(input())
    n=list(map(int,input().split()))
    n=list(set(n))
    index=a-len(n)
    if index%2==0:
        count=index//2
        answer=a-2*count
    else:
        count=index//2+1
        answer=a-2*count
    print(answer)