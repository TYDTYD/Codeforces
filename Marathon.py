import sys
input=sys.stdin.readline

T=int(input())

for i in range(T):
    a,b,c,d=map(int,input().split())
    count=0
    if a<b:
        count+=1
    if a<c:
        count+=1
    if a<d:
        count+=1

    print(count)